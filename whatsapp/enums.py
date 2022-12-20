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
    header = "header"
    body = "body"
    button = "button"


class ComponentSubType(Type):
    quick_reply = "quick_reply"
    url = "url"


class HeaderType(Type):
    document = "document"
    image = "image"
    text = "text"
    video = "video"


class InfoType(Type):
    home = "HOME"
    work = "WORK"


class InteractiveType(Type):
    button = "button"
    button_reply = "button_reply"
    list = "list"
    list_reply = "list_reply"
    product = "product"
    product_list = "product_list"


class MediaType(Type):
    image = "image"
    video = "video"


class MessageType(Type):
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
    business_initiated = "business_initiated"
    user_initiated = "user_initiated"
    referral_conversion = "referral_conversion"


class ParameterType(Type):
    currency = "currency"
    date_time = "date_time"
    document = "document"
    image = "image"
    text = "text"
    video = "video"


class PhoneType(Type):
    home = "HOME"
    work = "WORK"
    cell = "CELL"
    main = "MAIN"
    iphone = "IPHONE"


class PricingType(Type):
    CBP = "CBP"


class SourceType(Type):
    ad = "ad"
    post = "post"


class StatusType(Type):
    deleted = "deleted"
    delivered = "delivered"
    failed = "failed"
    read = "read"
    sent = "sent"


class SystemUpdateType(Type):
    customer_changed_number = "customer_changed_number"
    customer_identity_changed = "customer_identity_changed"
