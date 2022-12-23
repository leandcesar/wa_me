#!/usr/bin/env python

from typing import Any, Dict, Optional, Union

import requests

__all__ = (
    "WhatsappException",
    "ValidationError",
    "HTTPException",
    "BadRequest",
    "Unauthorized",
    "Forbidden",
    "NotFound",
    "WhatsappServerError",
)


class WhatsappException(Exception):
    """Base exception class for whatsapp-py."""


class ValidationError(WhatsappException):
    """An Exception that is raised when there is a Validation Error."""


class HTTPException(WhatsappException):
    """Exception that's raised when an HTTP request operation fails.

    Parameters
    ----------
    response: :class:`requests.Response`
        The response of the failed HTTP request. This is an instance of :class:`requests.Response`.
    content: Optional[Union[:class:`str`, Dict[:class:`str`, Any]]]
        The content response of the failed HTTP request.

    Attributes
    ----------
    status: :class:`int`
        The status code of the HTTP request.
    code: :class:`int`
        The WhatsApp Business Cloud API specific error code for the failure.
    subcode: :class:`int`
        The WhatsApp Business Cloud API specific error subcode for the failure.
    text: Optional[:class:`str`]
        The text of the error. Could be an empty string.
    type: Optional[:class:`str`]
        The type of the error. Could be an empty string.
    """

    def __init__(self, response: requests.Response, content: Optional[Union[str, Dict[str, Any]]]) -> None:
        self.response: requests.Response = response
        self.status: int = response.status_code
        self.code: int
        self.subcode: int
        self.text: str
        self.type: Optional[str]
        if isinstance(content, dict):
            self.code = content.get("code", 0)
            self.subcode = content.get("error_subcode", 0)
            self.type = content.get("type", 0)
            base = content.get("message", "")
            error_data: Optional[Dict[str, str]] = content.get("error_data")
            if error_data:
                details = error_data.get("details")
                self.text = f"{base}\n{details}"
            else:
                self.text = base
        else:
            self.code = 0
            self.subcode = 0
            self.text = content or ""
            self.type = ""
        e = f"{self.response.status_code} {self.response.reason} (error code: {self.code} subcode: {self.subcode})"
        if len(self.text):
            e += f": {self.text}"
        super().__init__(e)


class BadRequest(HTTPException):
    """Exception that's raised for when status code 400 occurs."""


class Unauthorized(HTTPException):
    """Exception that's raised for when status code 401 occurs."""


class Forbidden(HTTPException):
    """Exception that's raised for when status code 403 occurs."""


class NotFound(HTTPException):
    """Exception that's raised for when status code 404 occurs."""


class WhatsappServerError(HTTPException):
    """Exception that's raised for when a 500 range status code occurs."""
