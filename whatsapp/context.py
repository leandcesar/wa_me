#!/usr/bin/env python

from typing import Any, Dict, List, Optional

from datetime import datetime

from .bot import Bot
from .utils.converter import as_dict, from_dict
from .classes.enums import HeaderType, InteractiveType, MessageType
from .classes.events import Event, Value
from .classes.messages import (
    Action,
    Audio,
    Body,
    Button,
    Contact,
    Context,
    Document,
    Footer,
    Header,
    Image,
    Interactive,
    Location,
    Message,
    Reaction,
    Reply,
    Row,
    Section,
    Sticker,
    Text,
    Video,
)
from .classes.responses import Media, Readed, Response

__all__ = ("Ctx",)


class Ctx:
    def __init__(self, bot: Bot, data: Dict[str, Any]) -> None:
        event = from_dict(Event, data)
        self._bot: Bot = bot
        self._event: Event = event
        self._event_value: Value = event.entry[0].changes[0].value
        self._readed: bool = False
        self._reactions: List[str] = []
        self._responses: List[Response] = []

    @property
    def bot(self) -> Bot:
        return self._bot

    @property
    def event(self) -> Event:
        return self._event

    @property
    def readed(self) -> bool:
        return self._readed

    @property
    def reacted(self) -> bool:
        return bool(self._reactions)

    @property
    def replied(self) -> bool:
        return bool(self._responses)

    @property
    def phone_id(self) -> str:
        return self._event_value.metadata.phone_number_id

    @property
    def recipient_id(self) -> Optional[str]:
        if self._event_value.contacts:
            return self._event_value.contacts[0].wa_id
        elif self._event_value.messages:
            return self._event_value.messages[0].sender
        elif self._event_value.statuses:
            return self._event_value.statuses[0].recipient_id
        return None

    @property
    def recipient_name(self) -> Optional[str]:
        if self._event_value.contacts:
            return self._event_value.contacts[0].profile.name
        return None

    @property
    def is_error(self) -> bool:
        return bool(self._event_value.errors)

    @property
    def is_message(self) -> bool:
        return bool(self._event_value.messages)

    @property
    def is_status(self) -> bool:
        return bool(self._event_value.statuses)

    @property
    def timestamp(self) -> Optional[int]:
        if self.is_message:
            return self._event_value.messages[0].timestamp
        elif self.is_status:
            return self._event_value.statuses[0].timestamp
        return None

    @property
    def datetime(self) -> Optional[datetime]:
        if self.timestamp:
            return datetime.utcfromtimestamp(self.timestamp)
        return None

    @property
    def received_at(self) -> Optional[float]:
        if self.datetime:
            delta = datetime.utcnow() - self.datetime
            return delta.total_seconds()
        return None

    def media_url(self) -> Optional[str]:
        if not self.is_message:
            return None
        message_type: str = self._event_value.messages[0].type.value
        media = getattr(self._event_value.messages[0], message_type)
        if not hasattr(media, "mime_type"):  # media's check
            return None
        data = self.bot.http.fetch_media_url(media.id)
        response = from_dict(Media, data)
        return response.url

    def media(self) -> Optional[bytes]:
        media_url = self.media_url()
        if not media_url:
            return None
        return self.bot.http.download_media(media_url)

    def read(self) -> bool:
        if not self.is_message:
            return False
        if self.readed:
            return True
        message_id = self._event_value.messages[0].id
        data = self.bot.http.read_message(message_id)
        response = from_dict(Readed, data)
        self._readed = response.success
        return response.success

    def send_message(self, message: Message) -> Response:
        data = self.bot.http.send_message(as_dict(message))
        response = from_dict(Response, data)
        return response

    def react(self, emoji: str) -> Optional[Response]:
        if not self.is_message or not self.recipient_id:
            return None
        message_id = self._event_value.messages[0].id
        reaction = Reaction(emoji=emoji, message_id=message_id)
        message = Message(to=self.recipient_id, reaction=reaction, type=MessageType.reaction)
        response = self.send_message(message)
        if emoji:
            self._reactions.append(emoji)
        elif not emoji:
            self._reactions.clear()
        return response

    def unreact(self) -> Optional[Response]:
        return self.react("")

    def send(
        self,
        message: Optional[Message] = None,
        *,
        text: Optional[str] = None,
        audio_id: Optional[str] = None,
        audio_url: Optional[str] = None,
        contacts_data: List[Dict[str, Any]],
        document_id: Optional[str] = None,
        document_url: Optional[str] = None,
        image_id: Optional[str] = None,
        image_url: Optional[str] = None,
        interactive_data: Dict[str, Any],
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        address: Optional[str] = None,
        name: Optional[str] = None,
        options: Optional[List[Dict[str, Any]]] = None,
        quick_responses: Optional[List[Dict[str, Any]]] = None,
        sticker_id: Optional[str] = None,
        sticker_url: Optional[str] = None,
        video_id: Optional[str] = None,
        video_url: Optional[str] = None,
        caption: Optional[str] = None,
        filename: Optional[str] = None,
        button: Optional[str] = None,
        title: Optional[str] = None,
        header_text: Optional[str] = None,
        footer_text: Optional[str] = None,
        reply_to: Optional[str] = None,
    ) -> Optional[Response]:
        if not self.recipient_id:
            return None
        if message and isinstance(message, Message):
            pass
        elif text and not quick_responses and not options:
            message = Message(to=self.recipient_id, text=Text(body=text), type=MessageType.text)
        elif text and quick_responses:
            message = Message(
                to=self.recipient_id,
                interactive=Interactive(
                    action=Action(
                        buttons=[Button(reply=Reply(**quick_reply)) for quick_reply in quick_responses]
                    ),
                    body=Body(text=text),
                    type=InteractiveType.button,
                ),
                type=MessageType.interactive,
            )
        elif text and options:
            message = Message(
                to=self.recipient_id,
                interactive=Interactive(
                    action=Action(
                        button=button,
                        sections=[Section(rows=[Row(**option) for option in options], title=title)],
                    ),
                    body=Body(text=text),
                    header=Header(type=HeaderType.text, text=Text(body=header_text)) if header_text else None,
                    footer=Footer(text=footer_text) if footer_text else None,
                    type=InteractiveType.list,
                ),
                type=MessageType.interactive
            )
        elif audio_id or audio_url:
            message = Message(to=self.recipient_id, audio=Audio(id=audio_id, link=audio_url), type=MessageType.audio)
        elif contacts_data:
            message = Message(to=self.recipient_id, contacts=[Contact(**contact) for contact in contacts_data], type=MessageType.contacts)
        elif document_id or document_url:
            message = Message(to=self.recipient_id, document=Document(id=document_id, link=document_url, caption=caption, filename=filename), type=MessageType.document)
        elif image_id or image_url:
            message = Message(to=self.recipient_id, image=Image(id=image_id, link=image_url, caption=caption), type=MessageType.image)
        elif interactive_data:
            message = Message(to=self.recipient_id, interactive=Interactive(**interactive_data), type=MessageType.interactive)
        elif latitude and longitude:
            message = Message(to=self.recipient_id, location=Location(latitude=latitude, longitude=longitude, address=address, name=name), type=MessageType.location)
        elif sticker_id or sticker_url:
            message = Message(to=self.recipient_id, sticker=Sticker(id=sticker_id, link=sticker_url), type=MessageType.sticker)
        elif video_id or video_url:
            message = Message(to=self.recipient_id, video=Video(id=video_id, link=video_url, caption=caption), type=MessageType.video)
        else:
            raise Exception()

        if reply_to:
            message.context = Context(message_id=reply_to)

        response = self.send_message(message)
        self._responses.append(response)
        return response

    def reply(self, **kwargs) -> Optional[Response]:
        message_id = self._event_value.messages[0].id
        return self.send(reply_to=message_id, **kwargs)
