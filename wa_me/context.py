#!/usr/bin/env python

from typing import Any, Dict, List, Optional

from datetime import datetime

from .classes import enums, events, messages, responses
from .core.client import Client
from .core.converter import as_dict, from_dict

__all__ = ("Ctx",)


class Ctx:
    def __init__(self, client: Client, data: Dict[str, Any]) -> None:
        event = from_dict(events.Event, data)
        self._client: Client = client
        self._event: events.Event = event
        self._event_value: events.Value = event.entry[0].changes[0].value
        self._readed: bool = False
        self._reactions: List[str] = []
        self._replies: List[messages.Message] = []
        self._replies_ids: List[str] = []

    @property
    def client(self) -> Client:
        return self._client

    @property
    def event(self) -> events.Event:
        return self._event

    @property
    def readed(self) -> bool:
        return self._readed

    @property
    def reactions(self) -> List[str]:
        return self._reactions

    @property
    def replies(self) -> List[messages.Message]:
        return self._replies

    @property
    def replies_ids(self) -> List[str]:
        return self._replies_ids

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
    def error(self) -> Optional[events.Error]:
        if self._event_value.errors:
            return self._event_value.errors[0]
        return None

    @property
    def message(self) -> Optional[events.Message]:
        if self._event_value.messages:
            return self._event_value.messages[0]
        return None

    @property
    def status(self) -> Optional[events.Status]:
        if self._event_value.statuses:
            return self._event_value.statuses[0]
        return None

    @property
    def timestamp(self) -> Optional[int]:
        if self.message:
            return int(self.message.timestamp)
        elif self.status:
            return int(self.status.timestamp)
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
        if not self.message:
            return None
        message_type: str = self.message.type.value
        media = getattr(self.message, message_type)
        if not hasattr(media, "mime_type"):  # media's check
            return None
        data = self.client.http.fetch_media_url(media.id)
        response = from_dict(responses.Media, data)
        return response.url

    def media(self) -> Optional[bytes]:
        media_url = self.media_url()
        if not media_url:
            return None
        return self.client.http.download_media(media_url)

    def read(self) -> bool:
        if not self.message:
            return False
        if self.readed:
            return True
        message_id = self.message.id
        data = self.client.http.read_message(message_id)
        response = from_dict(responses.Readed, data)
        self._readed = response.success
        return response.success

    def send_message(self, message: messages.Message) -> responses.Response:
        data = self.client.http.send_message(as_dict(message))
        response = from_dict(responses.Response, data)
        return response

    def react(self, emoji: str) -> Optional[responses.Response]:
        if not self.message or not self.recipient_id:
            return None
        message_id = self.message.id
        reaction = messages.Reaction(emoji=emoji, message_id=message_id)
        message = messages.Message(
            to=self.recipient_id,
            reaction=reaction,
            type=enums.MessageType.reaction,
        )
        response = self.send_message(message)
        if emoji:
            self._reactions.append(emoji)
        elif not emoji:
            self._reactions.clear()
        return response

    def unreact(self) -> Optional[responses.Response]:
        return self.react("")

    def send(
        self, message: messages.Message, *, mention: bool = False
    ) -> responses.Response:
        if mention and self.message:
            message.context = messages.Context(message_id=self.message.id)
        response = self.send_message(message)
        self._replies.append(message)
        self._replies_ids.append(response.messages[0].id)
        return response

    def send_audio(
        self,
        audio_id: Optional[str] = None,
        audio_url: Optional[str] = None,
        *,
        mention: bool = False,
    ) -> Optional[responses.Response]:
        if not self.recipient_id:
            return None
        message = messages.Message(
            to=self.recipient_id,
            audio=messages.Audio(id=audio_id, link=audio_url),
            type=enums.MessageType.audio,
        )
        return self.send(message, mention=mention)

    def send_contacts(
        self, contacts_data: List[Dict[str, Any]], *, mention: bool = False
    ) -> Optional[responses.Response]:
        if not self.recipient_id:
            return None
        message = messages.Message(
            to=self.recipient_id,
            contacts=[messages.Contact(**contact) for contact in contacts_data],
            type=enums.MessageType.contacts,
        )
        return self.send(message, mention=mention)

    def send_document(
        self,
        document_id: Optional[str] = None,
        document_url: Optional[str] = None,
        *,
        caption: Optional[str] = None,
        filename: Optional[str] = None,
        mention: bool = False,
    ) -> Optional[responses.Response]:
        if not self.recipient_id:
            return None
        message = messages.Message(
            to=self.recipient_id,
            document=messages.Document(
                id=document_id,
                link=document_url,
                caption=caption,
                filename=filename,
            ),
            type=enums.MessageType.document,
        )
        return self.send(message, mention=mention)

    def send_image(
        self,
        image_url: Optional[str] = None,
        image_id: Optional[str] = None,
        *,
        caption: Optional[str] = None,
        mention: bool = False,
    ) -> Optional[responses.Response]:
        if not self.recipient_id:
            return None
        message = messages.Message(
            to=self.recipient_id,
            image=messages.Image(id=image_id, link=image_url, caption=caption),
            type=enums.MessageType.image,
        )
        return self.send(message, mention=mention)

    def send_interactive(
        self,
        *,
        interactive_data: Dict[str, Any],
        mention: bool = False,
    ) -> Optional[responses.Response]:
        if not self.recipient_id:
            return None
        message = messages.Message(
            to=self.recipient_id,
            interactive=messages.Interactive(**interactive_data),
            type=enums.MessageType.interactive,
        )
        return self.send(message, mention=mention)

    def send_location(
        self,
        latitude: float,
        longitude: float,
        *,
        name: Optional[str] = None,
        address: Optional[str] = None,
        mention: bool = False,
    ) -> Optional[responses.Response]:
        if not self.recipient_id:
            return None
        message = messages.Message(
            to=self.recipient_id,
            location=messages.Location(
                latitude=latitude,
                longitude=longitude,
                address=address,
                name=name,
            ),
            type=enums.MessageType.location,
        )
        return self.send(message, mention=mention)

    def send_options(
        self,
        text: str,
        options: List[Dict[str, Any]],
        *,
        button: str,
        title: str,
        header_text: Optional[str] = None,
        footer_text: Optional[str] = None,
        mention: bool = False,
    ) -> Optional[responses.Response]:
        if not self.recipient_id:
            return None
        message = messages.Message(
            to=self.recipient_id,
            interactive=messages.Interactive(
                action=messages.Action(
                    button=button,
                    sections=[
                        messages.Section(
                            rows=[messages.Row(**option) for option in options],
                            title=title,
                        )
                    ],
                ),
                body=messages.Body(text=text),
                header=messages.Header(
                    type=enums.HeaderType.text,
                    text=messages.Text(body=header_text),
                )
                if header_text
                else None,
                footer=messages.Footer(text=footer_text) if footer_text else None,
                type=enums.InteractiveType.list,
            ),
            type=enums.MessageType.interactive,
        )
        return self.send(message, mention=mention)

    def send_quick_replies(
        self,
        text: str,
        quick_replies: List[Dict[str, Any]],
        *,
        mention: bool = False,
    ) -> Optional[responses.Response]:
        if not self.recipient_id:
            return None
        message = messages.Message(
            to=self.recipient_id,
            interactive=messages.Interactive(
                action=messages.Action(
                    buttons=[
                        messages.Button(reply=messages.Reply(**quick_reply))
                        for quick_reply in quick_replies
                    ]
                ),
                body=messages.Body(text=text),
                type=enums.InteractiveType.button,
            ),
            type=enums.MessageType.interactive,
        )
        return self.send(message, mention=mention)

    def send_sticker(
        self,
        sticker_id: Optional[str] = None,
        sticker_url: Optional[str] = None,
        *,
        mention: bool = False,
    ) -> Optional[responses.Response]:
        if not self.recipient_id:
            return None
        message = messages.Message(
            to=self.recipient_id,
            sticker=messages.Sticker(id=sticker_id, link=sticker_url),
            type=enums.MessageType.sticker,
        )
        return self.send(message, mention=mention)

    def send_text(
        self, content: str, *, mention: bool = False
    ) -> Optional[responses.Response]:
        if not self.recipient_id:
            return None
        message = messages.Message(
            to=self.recipient_id,
            text=messages.Text(body=content),
            type=enums.MessageType.text,
        )
        return self.send(message, mention=mention)

    def send_video(
        self,
        video_id: Optional[str] = None,
        video_url: Optional[str] = None,
        *,
        caption: Optional[str] = None,
        mention: bool = False,
    ) -> Optional[responses.Response]:
        if not self.recipient_id:
            return None
        message = messages.Message(
            to=self.recipient_id,
            video=messages.Video(id=video_id, link=video_url, caption=caption),
            type=enums.MessageType.video,
        )
        return self.send(message, mention=mention)
