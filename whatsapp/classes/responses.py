#!/usr/bin/env python

from dataclasses import dataclass
from typing import Literal, List, Optional

from .enums import *  # NOQA

__all__ = (
    "Readed",
    "Media",
    "BusinessProfile",
    "Data",
    "Profile",
    "ErrorData",
    "Error",
    "ResponseError",
    "Contact",
    "Message",
    "Response",
)


@dataclass
class Readed:
    """Readed object.

    Parameters
    ----------
    success: :class:`bool`
        Indicates whether a message was successfully read.
    """

    success: bool


@dataclass
class Media:
    """Business profile object.

    Parameters
    ----------
    messaging_product: :class:`str`
        The value is always "whatsapp".
    id: :class:`str`
        The media object ID.
    mime_type: :class:`str`
        Mime type of the media file.
    file_size: :class:`int`
        The media file size.
    sha256: :class:`str`
        Hash for the file.
    url: :class:`str`
        The protocol and URL of the media.
    """

    messaging_product: Literal["whatsapp"]
    id: str
    mime_type: str
    file_size: int
    sha256: str
    url: str


@dataclass
class BusinessProfile:
    """Business profile object.

    Parameters
    ----------
    messaging_product: :class:`str`
        The value is always "whatsapp".

    address: :class:`str`
        The address of the business.

        .. note::

            The maximum character limit for the string is 256.

    description: :class:`str`
        Description of the business.

        .. note::

            The maximum character limit for the string is 256.

    about: Optional[:class:`str`]
        The text to display in business profile's About section.

        .. note::

            The max length for the string is 139 characters.

    email: Optional[:class:`str`]
        The contact email address (in valid email format) of the business.

        .. note::

            The maximum character limit for the string is 128 characters.

    profile_picture_url: Optional[:class:`str`]
        The handle of the profile picture generated from a call.
    vertical: Optional[:class:`str`]
        The industry type of the business.

        .. note::

            This can be one of the accepted values:
                UNDEFINED, OTHER, AUTO, BEAUTY, APPAREL, EDU, ENTERTAIN, EVENT_PLAN,
                FINANCE, GROCERY, GOVT, HOTEL, HEALTH, NONPROFIT, PROF_SERVICES, RETAIL,
                TRAVEL, RESTAURANT, or NOT_A_BIZ.

    websites: Optional[List[:class:`str`]]
        The URLs associated with the business. For instance, a website, Facebook Page, or Instagram.

        .. note::

            There is a maximum of 2 websites with a maximum of 256 characters each.
    """

    messaging_product: Literal["whatsapp"]
    address: str
    description: str
    about: Optional[str]
    email: Optional[str]
    profile_picture_url: Optional[str]
    vertical: Optional[str]
    websites: Optional[List[str]]


@dataclass
class Data:
    """Information about a business profile.

    Parameters
    ----------
    business_profile: List[:class:`.BusinessProfile`]
        The value is always "whatsapp".
    """

    business_profile: BusinessProfile


@dataclass
class Profile:
    """Profile response object.

    Parameters
    ----------
    data: List[:class:`.Data`]
        The value is always "whatsapp".
    """

    data: List[Data]


@dataclass
class ErrorData:
    """Error details data object.

    Parameters
    ----------
    messaging_product: :class:`str`
        The value is always "whatsapp".
    details: :class:`str`
        Describes the detailed error messages to help you debug the error.
    """

    messaging_product: Literal["whatsapp"]
    details: str


@dataclass
class Error:
    """Error object.

    Parameters
    ----------
    code: :class:`int`
        Error code.

        .. note::

            For more information, refer to: https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes#error-codes

    error_subcode: :class:`int`
        The subcode of the error.
    fbtrace_id: :class:`str`
        For Facebook Support.
    message: :class:`str`
        The title of this error.
    type: :class:`str`
        The type of error.
    error_data: Optional[:class:`.ErrorData`]
        Error details data.
    """

    code: int
    error_subcode: int
    fbtrace_id: str
    message: str
    type: str
    error_data: Optional[ErrorData] = None


@dataclass
class ResponseError:
    """Error response object.

    Parameters
    ----------
    error: :class:`.Error`
        Error object.
    """

    error: Error


@dataclass
class Contact:
    """Contact object.

    Parameters
    ----------
    input: :class:`str`
        Contact phone number.
    wa_id: :class:`str`
        WhatsApp ID.
    """

    input: str
    wa_id: str


@dataclass
class Message:
    """Message object.

    Parameters
    ----------
    id: :class:`str`
        The ID for the message that was sent by the business
    """

    id: str


@dataclass
class Response:
    """Message response object.

    Parameters
    ----------
    messaging_product: :class:`str`
        The value is always "whatsapp".
    contacts: List[:class:`.Contact`]
        A list of contact object.
    messages: List[:class:`.Message`]
        Information about a message sent by the business
    """

    messaging_product: Literal["whatsapp"]
    contacts: List[Contact]
    messages: List[Message]
