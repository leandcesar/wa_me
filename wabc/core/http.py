#!/usr/bin/env python

import json
import logging
import sys
from typing import Any, Dict, Optional, Sequence, Union
from urllib.parse import quote as _uriquote

import requests

from .errors import (
    BadRequest,
    Forbidden,
    HTTPException,
    NotFound,
    Unauthorized,
    WhatsappServerError,
)

__all__ = (
    "Route",
    "HTTPClient",
)

_log = logging.getLogger(__name__)

API_VERSION: int = 15


class Route:
    """Represents an HTTP route to the WhatsApp Business Cloud API."""

    def __init__(self, method: str, path: str, **kwargs) -> None:
        self.path: str = path
        self.method: str = method
        url = self.base + self.path
        if kwargs:
            url = url.format_map(
                {
                    k: _uriquote(v) if isinstance(v, str) else v
                    for k, v in kwargs.items()
                }
            )
        self.url: str = url

    @property
    def base(self) -> str:
        return f"https://graph.facebook.com/v{API_VERSION}.0"


class HTTPClient:
    """Represents an HTTP client sending HTTP requests to the WhatsApp Business Cloud API."""

    def __init__(
        self,
        *,
        proxy: Optional[str] = None,
        proxy_auth: Optional[requests.auth.HTTPBasicAuth] = None,
    ) -> None:
        self._session: requests.Session  # filled in start
        self.phone_id: Optional[str] = None
        self.token: Optional[str] = None
        self.proxy: Optional[str] = proxy
        self.proxy_auth: Optional[requests.auth.HTTPBasicAuth] = proxy_auth

    def start(self, phone_id: str, token: str) -> Dict[str, Any]:
        self._session = requests.Session()
        last_phone_id, self.phone_id = self.phone_id, phone_id
        last_token, self.token = self.token, token
        try:
            data = self.fetch_business_profile()
        except HTTPException as e:
            self.phone_id = last_phone_id
            self.token = last_token
            raise HTTPException(e.response, "Improper phone_id and/or token has been passed.")
        return data

    def restart(self) -> None:
        self._session = requests.Session()

    def close(self) -> None:
        if self._session:
            self._session.close()

    def request(self, route: Route, **kwargs) -> Any:
        method = route.method
        url = route.url
        headers: dict[str, str] = {}
        if self.token is not None:
            headers["Authorization"] = f"Bearer {self.token}"
        if "json" in kwargs:
            headers["Content-Type"] = "application/json"
            if not isinstance(kwargs.get("json"), dict):
                kwargs["json"] = json.dumps(kwargs.pop("json"), separators=(",", ":"), ensure_ascii=True)
        kwargs["headers"] = headers

        if self.proxy is not None:
            kwargs["proxy"] = self.proxy
        if self.proxy_auth is not None:
            kwargs["proxy_auth"] = self.proxy_auth

        response: Optional[requests.Response] = None
        data: Optional[Union[Dict[str, Any], str]] = None

        try:
            with self._session.request(method, url, **kwargs) as response:
                try:
                    data = response.json()
                except requests.exceptions.JSONDecodeError:
                    data = response.text
                _log.debug(f"{method} {url} with {data!r} has returned {response.status_code}")
                if 200 <= response.status_code < 300:
                    return data
                elif response.status_code == 400:
                    raise BadRequest(response, data)
                elif response.status_code == 401:
                    raise Unauthorized(response, data)
                elif response.status_code == 403:
                    raise Forbidden(response, data)
                elif response.status_code == 404:
                    raise NotFound(response, data)
                elif response.status_code == 429:
                    raise HTTPException(response, data)
                elif response.status_code >= 500:
                    raise WhatsappServerError(response, data)
                else:
                    raise HTTPException(response, data)
        except OSError as e:
            raise e

        if response is not None:
            if response.status_code >= 500:
                raise WhatsappServerError(response, data)
            raise HTTPException(response, data)
        raise RuntimeError("Unreachable code in HTTP handling")

    def fetch_business_profile(self) -> Dict[str, Any]:
        route = Route("GET", "/{phone_id}/whatsapp_business_profile", phone_id=self.phone_id)
        return self.request(route)

    def send_message(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        route = Route("POST", "/{phone_id}/messages", phone_id=self.phone_id)
        return self.request(route, json=payload)

    def read_message(self, message_id: str) -> Dict[str, Any]:
        route = Route("POST", "/{phone_id}/messages", phone_id=self.phone_id)
        payload = {"messaging_product": "whatsapp", "status": "read", "message_id": message_id}
        return self.request(route, json=payload)

    def fetch_media_url(self, media_id: str) -> Dict[str, Any]:
        route = Route("GET", "/{media_id}", media_id=media_id)
        return self.request(route)

    def download_media(self, media_url: str) -> bytes:
        headers: dict[str, str] = {}
        if self.token is not None:
            headers["Authorization"] = f"Bearer {self.token}"
        with self._session.get(media_url, headers=headers) as response:
            _log.debug(f"GET {media_url} has returned {response.status_code}")
            if response.status_code == 200:
                return response.content
            elif response.status_code == 404:
                raise NotFound(response, "asset not found")
            elif response.status_code == 403:
                raise Forbidden(response, "cannot retrieve asset")
            else:
                raise HTTPException(response, "failed to get asset")
