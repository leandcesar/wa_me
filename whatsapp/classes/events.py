#!/usr/bin/env python

from dataclasses import dataclass
from typing import Literal, List, Optional

from .enums import *  # NOQA

__all__ = (
    "Text",
    "Button",
    "Media",
    "MediaWithCaption",
    "Audio",
    "Document",
    "Image",
    "Sticker",
    "Video",
    "Reaction",
    "Location",
    "Address",
    "Email",
    "Name",
    "Org",
    "Phone",
    "URL",
    "Contact",
    "Error",
    "Pricing",
    "Origin",
    "Conversation",
    "Status",
    "Product",
    "Order",
    "Reply",
    "ButtonReply",
    "ListReply",
    "Interactive",
    "System",
    "Referral",
    "Identity",
    "ReferredProduct",
    "Context",
    "Message",
    "Profile",
    "Customer",
    "Metadata",
    "Value",
    "Change",
    "Entry",
    "Event",
)


@dataclass
class Text:
    """Text object.

    Parameters
    ----------
    body: :class:`str`
        The text of the message.
    """

    body: str


@dataclass
class Button:
    """Button object.

    Parameters
    ----------
    payload: :class:`str`
        The payload for a button set up by the business that a customer clicked as part of an interactive message.
    text: :class:`str`
        Button text.
    """

    payload: str
    text: str


@dataclass
class Media:
    """Media with caption object.

    Parameters
    ----------
    id: :class:`str`
        The media object ID.
    mime_type: :class:`str`
        Mime type of the media file.
    """

    id: str
    mime_type: str


@dataclass
class MediaWithCaption(Media):
    """Media object.

    Parameters
    ----------
    caption: Optional[:class:`str`]
        Caption for the media.
    """

    caption: Optional[str] = None


@dataclass
class Audio(Media):
    """Audio object."""


@dataclass
class Document(MediaWithCaption):
    """Document object.

    Parameters
    ----------
    filename: :class:`str`
        Name for the file on the sender's device
    sha256: :class:`str`
        Hash for the file.
    """

    filename: Optional[str] = None
    sha256: Optional[str] = None


@dataclass
class Image(MediaWithCaption):
    """Image object.

    Parameters
    ----------
    sha256: :class:`str`
        Hash for the image.
    """

    sha256: Optional[str] = None


@dataclass
class Sticker(Media):
    """Image object.

    Parameters
    ----------
    animated: :class:`bool`
        Set to `true` if the sticker is animated; `false` otherwise.
    sha256: :class:`str`
        Hash for the sticker.
    """

    animated: bool
    sha256: Optional[str] = None


@dataclass
class Video(MediaWithCaption):
    """Document object.

    Parameters
    ----------
    filename: :class:`str`
        Name for the video on the sender's device
    sha256: :class:`str`
        Hash for the video.
    """

    filename: Optional[str] = None
    sha256: Optional[str] = None


@dataclass
class Reaction:
    """Document object.

    Parameters
    ----------
    emoji: :class:`str`
        The emoji used for the reaction.
    message_id: :class:`str`
        The WhatsApp Business Account ID of the message received that contained the reaction.
    """

    message_id: str
    emoji: Optional[str] = None


@dataclass
class Location:
    """Location object.

    Parameters
    ----------
    longitude: :class:`float`
        The longitude of the location.
    latitude: :class:`float`
        The latitude of the location.
    address: Optional[:class:`str`]
        The address of the location.
    name: Optional[:class:`str`]
        The name of the location.
    """

    latitude: float
    longitude: float
    address: Optional[str] = None
    name: Optional[str] = None


@dataclass
class Address:
    """Address object.

    Parameters
    ----------
    city: Optional[:class:`str`]
        The name of the city.
    country_code: Optional[:class:`str`]
        The two-letter country abbreviation.
    country: Optional[:class:`str`]
        The full name of the country.
    state: Optional[:class:`str`]
        The abbreviation name of the state.
    street: Optional[:class:`str`]
        Steet number and name.
    type: Optional[:class:`.InfoType`]
        Address type.
    zip: Optional[:class:`str`]
        The ZIP code.
    """

    city: Optional[str] = None
    country_code: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    street: Optional[str] = None
    type: Optional[InfoType] = None
    zip: Optional[str] = None


@dataclass
class Email:
    """Email object.

    Parameters
    ----------
    email: Optional[:class:`str`]
        Email address.
    type: Optional[:class:`.InfoType`]
        Email type.
    """

    email: Optional[str] = None
    type: Optional[InfoType] = None


@dataclass
class Name:
    """Name object.

    Parameters
    ----------
    formatted_name: :class:`str`
        Full name, as it normally appears.
    first_name: Optional[:class:`str`]
        First name.
    last_name: Optional[:class:`str`]
        Last name.
    middle_name: Optional[:class:`str`]
        Middle name.
    prefix: Optional[:class:`str`]
        Name prefix.
    suffix: Optional[:class:`str`]
        Name suffix.
    """

    formatted_name: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    prefix: Optional[str] = None
    suffix: Optional[str] = None


@dataclass
class Org:
    """Org object.

    Parameters
    ----------
    company: Optional[:class:`str`]
        Name of the contact's company.
    department: Optional[:class:`str`]
        Name of the contact's department.
    title: Optional[:class:`str`]
        The contact's business title.
    """

    company: Optional[str] = None
    department: Optional[str] = None
    title: Optional[str] = None


@dataclass
class Phone:
    """Phone object.

    Parameters
    ----------
    phone: Optional[:class:`str`]
        Contact phone number.
    type: Optional[:class:`.PhoneType`]
        Phone type.
    wa_id: Optional[:class:`str`]
        WhatsApp ID.
    """

    phone: Optional[str] = None
    type: Optional[PhoneType] = None
    wa_id: Optional[str] = None


@dataclass
class URL:
    """URL object.

    Parameters
    ----------
    type: Optional[:class:`.InfoType`]
        URL type.
    url: Optional[:class:`str`]
        The URL.
    """

    type: Optional[InfoType] = None
    url: Optional[str] = None


@dataclass
class Contact:
    """Contact object.

    Parameters
    ----------
    name: :class:`.Name`
        Specifies the name object.
    addresses: Optional[List[:class:`.Address`]]
        Specifies an array of address objects.
    birthday: Optional[:class:`str`]
        A `YYYY-MM-DD` formatted string.
    emails: Optional[List[:class:`.Email`]]
        Specifies an array of email objects.
    org: Optional[:class:`.Org`]
        Specifies the org object.
    phones: Optional[List[:class:`.Phone`]]
        Specifies an array of phone objects.
    urls: Optional[List[:class:`.URL`]]
        Specifies an array of url objects.
    """

    name: Name
    addresses: Optional[List[Address]] = None
    birthday: Optional[str] = None  # YYYY-MM-DD
    emails: Optional[List[Email]] = None
    org: Optional[Org] = None
    phones: Optional[List[Phone]] = None
    urls: Optional[List[URL]] = None


@dataclass
class Error:
    """Error object.

    Parameters
    ----------
    code: :class:`int`
        Error code.
    details: :class:`str`
        Error title.
    title: :class:`str`
        Error details.
    """

    code: Optional[int] = None
    details: Optional[str] = None
    title: Optional[str] = None


@dataclass
class Pricing:
    """Pricing object.
    
    Parameters
    ----------
    category: Optional[:class:`.OriginType`]
        Indicates the conversation pricing category.
    pricing_model: Optional[:class:`.PricingType`]
        Type of pricing model used by the business. Current supported value is CBP.
    """

    category: Optional[OriginType] = None
    pricing_model: Optional[PricingType] = None


@dataclass
class Origin:
    """Origin object.
    
    Parameters
    ----------
    type: :class:`.OriginType`
        Indicates where a conversation has started. This can also be referred to as a conversation entry point.
    """
    
    type: OriginType


@dataclass
class Conversation:
    """Conversation object.
    
    .. note:

        WhatsApp defines a conversation as a 24-hour session of messaging between a person and a business.
        There is no limit on the number of messages that can be exchanged in the fixed 24-hour window.
        The 24-hour conversation session begins when:
            - A business-initiated message is delivered to a customer
            - A business reply to a customer message is delivered
        The 24-hour conversation session is different from the 24-hour customer support window.
        The customer support window is a rolling window that is refreshed when a customer-initiated
        message is delivered to a business.
        Within the customer support window businesses can send free-form messages.
        Any business-initiated message sent more than 24 hours after the last customer message must be
        a template message.

    Parameters
    ----------
    id: :class:`str`
        Represents the ID of the conversation the given status notification belongs to.
    origin: :class:`.Origin`
        Indicates who initiated the conversation.
    expiration_timestamp: Optional[:class:`int`]
        Date when the conversation expires.

        .. note:

            This field is only present for messages with a status set to "sent".
    """

    id: str
    origin: Origin
    expiration_timestamp: Optional[str] = None


@dataclass
class Status:
    """Status object.
    
    id: :class:`str`
        The ID for the message that the business that is subscribed to the webhooks sent to a customer.
    recipient_id: :class:`str`
        The WhatsApp ID for the customer that the business, that is subscribed to the webhooks, sent to the customer.
    status: :class:`.StatusType`
        A webhook is triggered when a message received by a business has been status updated.
    timestamp: :class:`int`
        Date for the status message.
    conversation: Optional[:class:`.Conversation`]
        Information about the conversation.
    errors: Optional[List[:class:`.Error`]]
        A list of error objects.
    pricing: Optional[:class:`.Pricing`]
        An object containing billing information.
    """

    id: str
    recipient_id: str
    status: StatusType
    timestamp: str
    conversation: Optional[Conversation] = None
    errors: Optional[List[Error]] = None
    pricing: Optional[Pricing] = None


@dataclass
class Product:
    """Product object.

    Parameters
    ----------
    currency: :class:`str`
        Price currency.
    item_price: :class:`float`
        Price of each item.
    product_retailer_id: :class:`str`
        Unique identifier of the product in a catalog.
    quantity: :class:`int`
        Number of items.
    """

    currency: str
    item_price: float
    product_retailer_id: str
    quantity: int


@dataclass
class Order:
    """Order object.

    Parameters
    ----------
    catalog_id: :class:`str`
        ID for the catalog the ordered item belongs to.
    text: :class:`str`
        Text message from the user sent along with the order.
    product_items: Optional[List[:class:`.Product`]]
        A list of product item objects.
    """

    catalog_id: str
    text: str
    product_items: Optional[List[Product]] = None


@dataclass
class Reply:
    """Reply object for "list_reply".

    Parameters
    ----------
    id: :class:`str`
        Unique ID of a selected button or list item.
    title: :class:`str`
        Title of a selected button or list item.
    """

    id: str
    title: str


@dataclass
class ButtonReply(Reply):
    """Reply object for "button_reply"."""


@dataclass
class ListReply(Reply):
    """Reply object for "list_reply".

    Parameters
    ----------
    description: Optional[:class:`str`]
        Description of the selected row (only for list items).
    """

    description: Optional[str] = None

@dataclass
class Interactive:
    """Interactive object.

    Parameters
    ----------
    type: :class:`.InteractiveType`
        The type of the interactive message.
    button_reply: Optional[:class:`.ButtonReply`]
        Sent when a customer clicks a button.
    list_reply: Optional[:class:`.ListReply`]
        Sent when a customer selects an item from a list.
    """

    type: InteractiveType
    button_reply: Optional[ButtonReply] = None
    list_reply: Optional[ListReply] = None


@dataclass
class System:
    """System object.

    Parameters
    ----------
    body: :class:`str`
        Describes the change to the customer's identity or phone number.
    customer: :class:`str`
        The WhatsApp ID for the customer prior to the update.
    identity: :class:`str`
        Hash for the identity fetched from server.
    type: :class:`.SystemUpdateType`
        Type of system update.
    new_wa_id: Optional[:class:`str`]
        New WhatsApp ID for the customer when their phone number is updated.
    wa_id: Optional[:class:`str`]
        New WhatsApp ID for the customer when their phone number is updated.
    """

    body: str
    customer: str
    identity: str
    type: SystemUpdateType
    new_wa_id: Optional[str] = None
    wa_id: Optional[str] = None


@dataclass
class Referral:
    """Referral object.

    Parameters
    ----------
    body: :class:`str`
        Body for the ad or post.
    headline: :class:`str`
        Headline used in the ad or post.
    image_url: Optional[:class:`str`]
        URL of the image, when media_type is an image.
    media_type: :class:`.MediaType`
        Media present in the ad or post.
    source_id: :class:`str`
        Meta ID for an ad or a post.
    source_type: :class:`.SourceType`
        The type of the ad’s source.
    source_url: :class:`str`
        A customer clicked an ad that redirects them to WhatsApp, this object is included in the messages object.
    thumbnail_url: Optional[:class:`.str`]
        URL for the thumbnail, when media_type is a "video".
    video_url: Optional[:class:`.str`]
        URL of the video, when media_type is a "video".
    """

    body: str
    headline: str
    media_type: MediaType
    source_id: str
    source_type: SourceType
    source_url: str
    image_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    video_url: Optional[str] = None


@dataclass
class Identity:
    """Identity object.

    Parameters
    ----------
    acknowledged: :class:`bool`
        State of acknowledgment for the messages system "customer_identity_changed".
    created_timestamp: :class:`int`
        The time when the WhatsApp Business Management API detected the customer may have changed their profile information.
    hash: :class:`str`
        The ID for the messages system "customer_identity_changed".
    """

    acknowledged: bool
    created_timestamp: str
    hash: str


@dataclass
class ReferredProduct:
    """ReferredProduct object.

    Parameters
    ----------
    catalog_id: :class:`str`
        Unique identifier of the Meta catalog linked to the WhatsApp Business Account.
    product_retailer_id: :class:`str`
        Unique identifier of the product in a catalog.
    """

    catalog_id: str
    product_retailer_id: str


@dataclass
class Context:
    """Context object.

    Parameters
    ----------
    id: :class:`str`
        The message ID for the sent message for an inbound reply.
    forwarded: Optional[:class:`bool`]
        Set to true if the message received by the business has been forwarded.
    frequently_forwarded: Optional[:class:`bool`]
        Set to true if the message received by the business has been forwarded more than 5 times.
    referred_product: Optional[:class:`.ReferredProduct`]
        The product the user is requesting information about.

        .. note::

            Required for Product Enquiry Messages.

    sender: Optional[:class:`str`]
        The WhatsApp ID for the customer who replied to an inbound message.
    """

    id: str
    forwarded: Optional[bool] = None
    frequently_forwarded: Optional[bool] = None
    referred_product: Optional[ReferredProduct] = None
    sender: Optional[str] = None  # Original: from


@dataclass
class Message:
    """Message object.

    Parameters
    ----------
    id: :class:`str`
        The ID for the message that was received by the business.
    sender: :class:`str`
        The customer's phone number who sent the message to the business
    timestamp: :class:`int`
        The time when the customer sent the message to the business.
    type: :class:`.MessageType`
        The type of message that has been received by the business that has subscribed to Webhooks.
    audio: Optional[:class:`.Audio`]
        When the messages type is set to audio, including voice messages, this object is included in the messages object.
    button: Optional[:class:`.Button`]
        When the messages type field is set to button, this object is included in the messages object.
    contacts: Optional[List[:class:`.Contact`]]
        When messages type is set to contacts, this object is included in the messages object.
    context: Optional[:class:`.Context`]
        The context for a message that was forwarded or in an inbound reply from the customer.
    document: Optional[:class:`.Document`]
        When messages type is set to document, this object is included in the messages object.
    errors: Optional[List[:class:`.Error`]]
        The message that a business received from a customer is not a supported type.
    identity: Optional[:class:`.Identity`]
        A webhook is triggered when a customer's phone number or profile information has been updated.
    image: Optional[:class:`.Image`]
        When messages type is set to image, this object is included in the messages object.
    interactive: Optional[:class:`.Interactive`]
        When a customer selected a button or list reply, this object is included in the messages object.
    location: Optional[:class:`.Location`]
        When messages type is set to location, this object is included in the messages object.
    order: Optional[:class:`.Order`]
        Included in the messages object when a customer has placed an order.
    reaction: Optional[:class:`.Reaction`]
        When messages type is set to reaction, this object is included in the messages object.
    referral: Optional[:class:`.Referral`]
        A customer clicked an ad that redirects them to WhatsApp, this object is included in the messages object.
    sticker: Optional[:class:`.Sticker`]
        When messages type is set to sticker, this object is included in the messages object.
    system: Optional[:class:`.System`]
        When messages type is set to system, a customer has updated their phone number or profile information, this object is included in the messages object.
    text: Optional[:class:`.Text`]
        When messages type is set to text, the body of text is included in the messages object.
    video: Optional[:class:`.Video`]
        When messages type is set to video, this object is included in messages object.
    """

    id: str
    sender: str  # Original: from
    timestamp: str
    type: MessageType
    audio: Optional[Audio] = None
    button: Optional[Button] = None
    contacts: Optional[List[Contact]] = None
    context: Optional[Context] = None
    document: Optional[Document] = None
    errors: Optional[List[Error]] = None
    identity: Optional[Identity] = None
    image: Optional[Image] = None
    interactive: Optional[Interactive] = None
    location: Optional[Location] = None
    order: Optional[Order] = None
    reaction: Optional[Reaction] = None
    referral: Optional[Referral] = None
    sticker: Optional[Sticker] = None
    system: Optional[System] = None
    text: Optional[Text] = None
    video: Optional[Video] = None


@dataclass
class Profile:
    """Metadata for the business that is subscribed to the webhook.

    Parameters
    ----------
    name: :class:`str`
        The customer’s name.
    """

    name: Optional[str] = None


@dataclass
class Customer:
    """Customer object.

    Parameters
    ----------
    profile: :class:`.Profile`
        An object containing customer profile information
    wa_id: :class:`str`
        The customer's WhatsApp ID. A business can respond to a message using this ID.
    """

    profile: Profile
    wa_id: str


@dataclass
class Metadata:
    """Metadata for the business that is subscribed to the webhook.

    Parameters
    ----------
    display_phone_number: :class:`str`
        The phone number that is displayed for a business.
    phone_number_id: :class:`str`
        ID for the phone number. A business can respond to a message using this ID.
    """

    display_phone_number: str
    phone_number_id: str


@dataclass
class Value:
    """The value object contains details for the change that triggered the webhook.

    Parameters
    ----------
    messaging_product: :class:`str`
        The value is always "whatsapp".
    metadata: :class:`.Metadata`
        Metadata for the business.
    contacts: Optional[List[:class:`.Customer`]]
        A list of contacts objects with information for the customer who sent a message to the business.
    errors: Optional[List[:class:`.Error`]]
        A list of error objects with information received when a message failed.
    messages: Optional[List[:class:`.Message`]]
        Information about a message received by the business
    statuses: Optional[List[:class:`.Status`]]
        Status for a message that was sent by the business.
    """

    messaging_product: Literal["whatsapp"]
    metadata: Metadata
    contacts: Optional[List[Customer]] = None
    errors: Optional[List[Error]] = None
    messages: Optional[List[Message]] = None
    statuses: Optional[List[Status]] = None


@dataclass
class Change:
    """Change object.

    Webhooks are triggered when a customer performs an action
    or the status for a message a business sends a customer changes.

    Parameters
    ----------
    field: :class:`str`
        The type of notification. The only option for this API is "messages".
    value: :class:`.Value`
        The details for the changes.
    """

    field: Literal["messages"]
    value: Value


@dataclass
class Entry:
    """Entry object.

    Webhooks are triggered when a customer performs an action
    or the status for a message a business sends a customer changes.

    Parameters
    ----------
    id: :class:`str`
        The WhatsApp Business Account ID for the business that is subscribed to the webhook.
    changes: List[:class:`.Change`]
        A list of change object that triggered the webhook.
    """

    id: str
    changes: List[Change]


@dataclass
class Event:
    """Notification payload object.

    Webhooks are triggered when a customer performs an action
    or the status for a message a business sends a customer changes.

    Parameters
    ----------
    object: :class:`str`
        The specific webhook a business is subscribed to. The webhook is "whatsapp_business_account".
    entry: List[:class:`.Entry`]
        A list of entry object.
    """

    object: Literal["whatsapp_business_account"]
    entry: List[Entry]
