#!/usr/bin/env python

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from requests import Response

__all__ = (
    "WhatsappException",
    "HTTPException",
    "BadRequest",
    "Unauthorized",
    "Forbidden",
    "NotFound",
    "WhatsappServerError",
)


class WhatsappException(Exception):
    """Base exception class for whatsapp-py."""


class HTTPException(WhatsappException):
    """Exception that's raised when an HTTP request operation fails.

    Attributes
    ----------
    response: :class:`requests.Response`
        The response of the failed HTTP request. This is an instance of :class:`requests.Response`.
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

    def __init__(self, response: Response, message: Optional[Union[str, Dict[str, Any]]]) -> None:
        self.response: Response = response
        self.status: int = response.status_code
        self.code: int
        self.subcode: int
        self.text: Optional[str]
        self.type: Optional[str]
        if isinstance(message, dict):
            self.code = message.get("code", 0)
            self.subcode = message.get("error_subcode", 0)
            self.type = message.get("type", 0)
            base = message.get("message", "")
            error_data: Optional[Dict[str, str]] = message.get("error_data")
            if error_data:
                details = error_data.get("details")
                self.text = f"{base}\n{details}"
            else:
                self.text = base
        else:
            self.code = 0
            self.subcode = 0
            self.text = message or ""
            self.type = ""
        e = f"{self.response.status} {self.response.reason} (error code: {self.code} subcode: {self.subcode})"
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
