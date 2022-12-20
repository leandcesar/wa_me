#!/usr/bin/env python

from enum import Enum

__all__ = (
    "Type",
    "ComponentType",
    "ComponentSubType",
    "HeaderType",
    "InfoType",
    "InteractiveType",
    "MediaType",
    "MessageType",
    "OriginType",
    "ParameterType",
    "PhoneType",
    "PricingType",
    "SourceType",
    "StatusType",
    "SystemUpdateType",
)


class Type(str, Enum):
    ...


class ComponentType(Type):
    """Component type."""

    header = "header"
    body = "body"
    button = "button"


class ComponentSubType(Type):
    """Component subtype."""

    quick_reply = "quick_reply"
    url = "url"


class HeaderType(Type):
    """Message interactive header type."""

    document = "document"
    image = "image"
    text = "text"
    video = "video"


class InfoType(Type):
    """Information type."""

    home = "HOME"
    work = "WORK"


class InteractiveType(Type):
    """Message interactive type."""

    button = "button"
    button_reply = "button_reply"
    list = "list"
    list_reply = "list_reply"
    product = "product"
    product_list = "product_list"


class MediaType(Type):
    """Referral supported media type."""

    image = "image"
    video = "video"


class MessageType(Type):
    """Message type."""

    audio = "audio"
    button = "button"
    contacts = "contacts"
    document = "document"
    image = "image"
    interactive = "interactive"
    location = "location"
    order = "order"
    reaction = "reaction"
    sticker = "sticker"
    system = "system"
    template = "template"
    text = "text"
    unknown = "unknown"
    unsupported = "unsupported"
    video = "video"


class OriginType(Type):
    """Origin type.

    .. note::

        Indicates where a conversation has started.

        - "business_initiated": Indicates that the conversation started by a business
        sending the first message to a customer. This applies any time it has been
        more than 24 hours since the last customer message.

        - "customer_initiated": Indicates that the conversation started by a business
        replying to a customer message. This applies only when the business reply is
        within 24 hours of the last customer message.

        - "referral_conversion": Indicates that the conversation originated from
        a free entry point. These conversations are always customer-initiated.
    """

    business_initiated = "business_initiated"
    user_initiated = "user_initiated"
    referral_conversion = "referral_conversion"


class ParameterType(Type):
    """Component parameter type."""

    currency = "currency"
    date_time = "date_time"
    document = "document"
    image = "image"
    text = "text"
    video = "video"


class PhoneType(Type):
    """Phone information type."""

    home = "HOME"
    work = "WORK"
    cell = "CELL"
    main = "MAIN"
    iphone = "IPHONE"


class PricingType(Type):
    """Pricing type."""

    CBP = "CBP"


class SourceType(Type):
    """Referral source type."""

    ad = "ad"
    post = "post"


class StatusType(Type):
    """Status type."""

    deleted = "deleted"
    delivered = "delivered"
    failed = "failed"
    read = "read"
    sent = "sent"


class SystemUpdateType(Type):
    """System update type."""

    customer_changed_number = "customer_changed_number"
    customer_identity_changed = "customer_identity_changed"
