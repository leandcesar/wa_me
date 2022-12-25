#!/usr/bin/env python

from dataclasses import dataclass
from typing import Literal, List, Optional

from .enums import *  # NOQA

__all__ = (
    "Text",
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
    "Row",
    "Product",
    "Section",
    "Button",
    "Action",
    "Body",
    "Footer",
    "Header",
    "Interactive",
    "Currency",
    "DateTime",
    "Parameter",
    "Component",
    "Language",
    "Template",
    "Context",
    "Message",
)


@dataclass
class Text:
    """Text object.

    Parameters
    ----------
    body: :class:`str`
        The text of the text message that can contain URLs and supports formatting. Max: 4096 chars.
    preview_url: Optional[:class:`bool`]
        By default, WhatsApp recognizes URLs and makes them clickable,
        but you can also include a preview box with more information about the link.
        Set this field to true if you want to include a URL preview box.

        The majority of the time when you send a URL, whether with a preview or not,
        the receiver of the message will see a URL that they can click on.

        URL previews are only rendered after one of the following has occurred:
            - The business has sent a message template to the user.
            - The user initiates a conversation with a "click to chat" link.
            - The user adds the business phone number to their address book and initiates a conversation.
    """

    body: str
    preview_url: bool = False


@dataclass
class Media:
    """Media object.

    Parameters
    ----------
    id: Optional[:class:`str`]
        The media object ID. Required when you are not using a link.
    link: Optional[:class:`str`]
        The protocol and URL of the media to be sent. Required when you are not using an uploaded media ID.
    """

    id: Optional[str] = None
    link: Optional[str] = None


@dataclass
class MediaWithCaption(Media):
    """Media with caption object.

    Parameters
    ----------
    caption: Optional[:class:`str`]
        Describes the specified media. Max: 4096 chars.
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
    filename: Optional[:class:`str`]
        Describes the filename for the specific document.
    """

    filename: Optional[str] = None


@dataclass
class Image(MediaWithCaption):
    """Image object."""


@dataclass
class Sticker(Media):
    """Sticker object."""


@dataclass
class Video(MediaWithCaption):
    """Video object."""


@dataclass
class Reaction:
    """Reaction object.

    Parameters
    ----------
    emoji: :class:`str`
        The emoji used for the reaction. Set this value to "" (empty string) to remove the reaction.
    message_id: :class:`str`
        The WhatsApp Business Account ID that this reaction is being sent to.
    """

    emoji: str
    message_id: str


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
        The address of the location. This field is only displayed if `name` is present.
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

    .. note::

        At least one of the optional parameters needs to be included along with the `formatted_name` parameter.

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
        Automatically populated with the `wa_id` value as a formatted phone number.
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
class Row:
    """Row object.

    Parameters
    ----------
    id: :class`str`:
        Unique identifier row. Min: 1 char. Max: 200 chars.
    title: :class`str`:
        Row title. Min: 1 char. Max: 24 chars.
    description: Optional[:class`str`:]
        Row description. Min: 1 char. Max: 72 chars.
    """

    id: str
    title: str
    description: Optional[str] = None


@dataclass
class Product:
    """Product object.

    Parameters
    ----------
    product_retailer_id: :class`str`:
        Unique identifier of the product in a catalog.
    """

    product_retailer_id: str


@dataclass
class Section:
    """Section object.

    Parameters
    ----------
    product_items: Optional[List[:class`.Product`:]]
        A list of product object. Min: 1 item. Max: 30 items.

        .. note::

            Required for :class:`.InteractiveType.product_list`.

    rows: Optional[List[:class`.Row`:]]
        A list of row object. Min: 1 item. Max: 10 items.

        .. note::

            Required for :class:`.InteractiveType.list`.

    title: Optional[:class`str`:]
        Title of the section. Min: 1 char. Max: 24 chars.

        .. note::

            Required if the message has more than one section.
    """

    product_items: Optional[List[Product]] = None
    rows: Optional[List[Row]] = None
    title: Optional[str] = None


@dataclass
class Reply:
    """Reply object.

    Parameters
    ----------
    id: :class`str`:
        Unique identifier button. This ID is returned in the webhook when the button is clicked by the user. Min: 1 char. Max: 256 chars.
    title: :class`str`:
        Button title.

        .. note::

            It cannot be an empty string and must be unique within the message.
            Emojis are supported, markdown is not.
    """

    id: str
    title: str


@dataclass
class Button:
    """Button object.

    Parameters
    ----------
    id: :class`str`:
        Unique identifier button. This ID is returned in the webhook when the button is clicked by the user. Min: 1 char. Max: 256 chars.
    title: :class`str`:
        Button title.

        .. note::

            It cannot be an empty string and must be unique within the message.
            Emojis are supported, markdown is not.

    type: :class`str`:
        Button type. The only supported option is "reply". Min: 1 char. Max: 20 chars.
    """

    reply: Reply
    type: Literal["reply"] = "reply"


@dataclass
class Action:
    """Action object.

    Parameters
    ----------
    button: Optional[:class:`str`]
        The button content. Min: 1 char. Max: 20 chars.

        .. note::

            Required for :class:`.InteractiveType.list`.
            It cannot be an empty string and must be unique within the message.
            Does not allow emojis or markdown.

    buttons: Optional[List[:class:`.Button`]]
        A list of button object. Min: 1 item. Max: 3 items.

        .. note::

            Required for :class:`.InteractiveType.button_reply`.

    catalog_id: Optional[:class:`str`]
        Unique identifier of the Facebook catalog linked to your WhatsApp Business Account.

        .. note::

            Required for :class:`.InteractiveType.product` and  :class:`.InteractiveType.product_list`.

    product_retailer_id: Optional[:class:`str`]
        The unique identifier of the product in the catalog.

        .. note::

            Required for :class:`.InteractiveType.product` and  :class:`.InteractiveType.product_list`.

    sections: Optional[List[:class:`.Section`]]
        A list of section object. Min: 1 item. Max: 10 items.

        .. note::

            Required for :class:`.InteractiveType.list` and  :class:`.InteractiveType.product_list`.
    """

    button: Optional[str] = None
    buttons: Optional[List[Button]] = None
    catalog_id: Optional[str] = None
    product_retailer_id: Optional[str] = None
    sections: Optional[List[Section]] = None


@dataclass
class Body:
    """Body object.

    Parameters
    ----------
    text: :class:`str`
        The text field for the body object, supports Emojis and markdown. Max: 1024 chars.
    """

    text: str


@dataclass
class Footer:
    """Footer object.

    Parameters
    ----------
    text: :class:`str`
        The text field for the footer object, supports Emojis and markdown. Max: 60 chars.
    """

    text: str


@dataclass
class Header:
    """Header object.

    Parameters
    ----------
    type: :class:`.HeaderType`
        The header type.
    document: Optional[:class:`.Document`]
        A media object containing a document. Required if type is set to :class:`.HeaderType.document`
    image: Optional[:class:`.Image`]
        A media object containing a image. Required if type is set to :class:`.HeaderType.image`
    text: Optional[:class:`.Text`]
        A media object containing a text. Required if type is set to :class:`.HeaderType.text`
    video: Optional[:class:`.Video`]
        A media object containing a video. Required if type is set to :class:`.HeaderType.video`
    """

    type: HeaderType
    document: Optional[Document] = None
    image: Optional[Image] = None
    text: Optional[Text] = None
    video: Optional[Video] = None


@dataclass
class Interactive:
    """Interactive object.

    Parameters
    ----------
    type: :class:`.InteractiveType`
        The type of interactive message.
    action: :class:`.Action`
        The action you want the user to perform after reading the message.
    body: Optional[:class:`.Body`]
        The body of the message.

        .. note::

            Optional for type :class:`.InteractiveType.product`.
            Required for all other message types.

    footer: Optional[:class:`.Footer`]
        The footer of the message.
    header: Optional[:class:`.Header`]
        The header content displayed on top of the message.

        .. note::

            Required for type :class:`.InteractiveType.product_list`.
            Optional for other types.
            You cannot set a header if your interactive object is type :class:`.InteractiveType.product`.
    """

    type: InteractiveType
    action: Action
    body: Optional[Body] = None
    footer: Optional[Footer] = None
    header: Optional[Header] = None


@dataclass
class Currency:
    """Currency object.

    Parameters
    ----------
    amount_1000: :class:`int`
        Amount multiplied by 1000.
    code: :class:`str`
        Currency code as defined in ISO 4217.
    fallback_value: :class:`str`
        Default text if localization fails.
    """
    amount_1000: int
    code: str
    fallback_value: str


@dataclass
class DateTime:
    """DateTime object.

    Parameters
    ----------
    fallback_value: :class:`str`
        Default text.
    """
    fallback_value: str


@dataclass
class Parameter:
    """Parameter object.

    Parameters
    ----------
    type: :class:`.ParameterType`
        Indicates the type of parameter for the button.
    currency: Optional[:class:`.Currency`]
        A currency object.
    date_time: Optional[:class:`.DateTime`]
        A date_time object.
    document: Optional[:class:`.Document`]
        A media object containing a document.

        .. note:

            Only PDF documents are supported for media-based message templates.
            Captions not supported when used in a media template.

    image: Optional[:class:`.Image`]
        A media object containing a image.

        .. note:

            Captions not supported when used in a media template.

    text: Optional[:class:`str`]
        The message’s text.

        .. note:

            Character limit varies based on the following included component type.

            For the "header" component type: 60 characters
            For the "body" component type:
                - 1024 characters if other component types are included
                - 32768 characters if body is the only component type included

    video: Optional[:class:`.Video`]
        A media object containing a video.

        .. note:

            Captions not supported when used in a media template.
    """
    type: ParameterType
    currency: Optional[Currency] = None
    date_time: Optional[DateTime] = None
    document: Optional[Document] = None
    image: Optional[Image] = None
    text: Optional[str] = None
    video: Optional[Video] = None


@dataclass
class Component:
    """Component object.

    Parameters
    ----------
    type: :class:`.ComponentType`
        Describes the component type.
    sub_type: Optional[:class:`.ComponentSubType`]
        Type of button to create.

        .. note::

            Required when type is "button". Not used for the other types.

    parameters: Optional[List[:class:`.Parameter`]]
        List of parameter objects with the content of the message.

        .. note::

            Required when type is "button". Not used for the other types.

    index: Optional[:class:`str`]
        Position index of the button.

        .. note::

            Required when type is "button". Not used for the other types.
            You can have up to 3 buttons using index values of 0 to 2.
    """

    type: ComponentType
    sub_type: Optional[ComponentSubType] = None
    parameters: Optional[List[Parameter]] = None
    index: Optional[str] = None


@dataclass
class Language:
    """Language object.

    Parameters
    ----------
    code: :class:`str`
        The code of the language or locale to use.

        .. note::

            This field accepts both `language` (for example, "en") and `language_locale` (for example, "en_US") formats.

    policy: :class:`str`
        Language policy option.

        .. note::

            Default (and only supported value): `deterministic`
    """

    code: str
    policy: Literal["deterministic"] = "deterministic"


@dataclass
class Template:
    """Template object.

    Parameters
    ----------
    name: :class:`str`
        The name of the template.
    language: :class:`.Language`
        Specifies a language object. Specifies the language the template may be rendered in.

        .. note::

            Only the `deterministic` language policy works with media template messages.

    components: Optional[:class:`.Component`]
        A list of component object.
    """

    name: str
    language: Language
    components: Optional[List[Component]] = None


@dataclass
class Context:
    """Context object.

    Parameters
    ----------
    message_id: :class:`str`
        The WhatsApp Business Account ID for the message you want to reply.
    """

    message_id: str


@dataclass
class Message:
    """Message object to send a message.

    Parameters
    ----------
    to: :class:`str`
        WhatsApp ID or phone number for the person you want to send a message to.
    messaging_product: :class:`str`
        Sender service used for the request. Always use "whatsapp".
    recipient_type: :class:`str`
        Currently, you can only send messages to individuals. Set this value to "individual".
    context: Optional[:class:`.Context`]
        Used to mention a specific message you are replying to.
    type: Optional[:class:`.MessageType`]
        The type of message you want to send.
    audio: :class:`.Audio`
        A media object containing audio.
    contacts: List[:class:`.Contact`]
        A list of contact object.
    document: :class:`.Document`
        A media object containing a document.
    image: :class:`.Image`
        A media object containing a image.
    interactive: :class:`.Interactive`
        A interactive object.
    location: :class:`.Location`
        A location object.
    reaction: :class:`.Reaction`
        A reaction object.
    sticker: :class:`.Sticker`
        A sticker object.
    template: :class:`.Template`
        A template object.
    text: :class:`.Text`
        A text object.
    video: :class:`.Video`
        A media object containing a video.
    message_id: :class:`str`
        The WhatsApp Business Account ID for the message you want to mark as read.
    status: :class:`.StatusType`
        Status message. Set this value to "read".
    """

    to: str
    messaging_product: Literal["whatsapp"] = "whatsapp"
    recipient_type: Literal["individual"] = "individual"
    context: Optional[Context] = None
    type: Optional[MessageType] = None
    audio: Optional[Audio] = None
    contacts: Optional[List[Contact]] = None
    document: Optional[Document] = None
    image: Optional[Image] = None
    interactive: Optional[Interactive] = None
    location: Optional[Location] = None
    reaction: Optional[Reaction] = None
    sticker: Optional[Sticker] = None
    template: Optional[Template] = None
    text: Optional[Text] = None
    video: Optional[Video] = None
    message_id: Optional[str] = None
    status: Optional[StatusType] = None
