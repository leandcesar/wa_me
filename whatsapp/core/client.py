#!/usr/bin/env python

from typing import Optional

import requests

from .http import HTTPClient

__all__ = ("Client",)


class Client:
    """Represents a client connection that connects to Whatsapp.
    This class is used to interact with the WhatsApp Business Cloud API.

    .. note::

        The Cloud API supports up to 80 messages per second (mps) combined sending and
        receiving of text and media messages by default, and up to 500 mps by request.

    .. note::

        Cloud API follows Business Use Case Rate Limits. Each WhatsApp Business Account (WABA) has
        a call count rate limit and each call made by your app counts toward the limit.
        An app’s call count for a WABA is the number of calls it can make to business accounts under
        this WABA during a rolling one hour window and is calculated as follows:

            Calls within one hour for a WABA = 1800000 * Number of Registered Numbers under this WABA

        You will receive an 80007 error code when you hit call limits.
    """

    def __init__(self, **kwargs) -> None:
        proxy: Optional[str] = kwargs.pop("proxy", None)
        proxy_auth: Optional[requests.auth.HTTPBasicAuth] = kwargs.pop("proxy_auth", None)
        self.http: HTTPClient = HTTPClient(proxy=proxy, proxy_auth=proxy_auth)
        self._closed: bool = False

    def start(self, phone_id: str, token: str) -> None:
        """Starts the internal HTTP session of the client.

        Parameters
        ----------
        phone_id: :class:`str`
            ID for the phone number connected to the WhatsApp Business API.
        token: :class:`str`
            Your user access token after signing up at developers.facebook.com.
        """
        self.http.start(phone_id.strip(), token.strip())

    def close(self) -> None:
        """Closes the internal HTTP session."""
        if self._closed:
            return
        self._closed = True
        self.http.close()

    def clear(self) -> None:
        """Clears the internal HTTP session."""
        self._closed = False
        self.http.restart()

    def is_closed(self) -> bool:
        """Indicates if the internal HTTP session is closed."""
        return self._closed
