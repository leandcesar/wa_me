from typing import List, Optional

from whatsapp import Bot, Ctx

__all__ = ("MirrorBot",)


class MirrorBot(Bot):

    def before_event_message(self, ctx: Ctx) -> None:
        ctx.read()

    def on_event_message_audio(self, ctx: Ctx) -> None:
        ctx.send(audio_id=ctx.message.audio.id)

    def on_event_message_contacts(self, ctx: Ctx) -> None:
        contacts_data = [
            {
                "name": {
                    "formatted_name": contact.name.formatted_name,
                    "first_name": contact.name.first_name,
                },
                "phones": [
                    {
                        "phone": phone.phone,
                        "type": phone.type,
                        "wa_id": phone.wa_id,
                    }
                    for phone in contact.phones
                ],
            }
            for contact in ctx.message.contacts
        ]
        ctx.send(contacts_data=contacts_data)

    def on_event_message_document(self, ctx: Ctx) -> None:
        ctx.send(document_id=ctx.message.document.id, caption=ctx.message.document.caption, filename=ctx.message.document.filename)

    def on_event_message_image(self, ctx: Ctx) -> None:
        ctx.send(image_id=ctx.message.image.id, caption=ctx.message.image.caption)

    def on_event_message_location(self, ctx: Ctx) -> None:
        ctx.send(
            latitude=ctx.message.location.latitude,
            longitude=ctx.message.location.longitude,
            address=ctx.message.location.address,
            name=ctx.message.location.name,
        )

    def on_event_message_sticker(self, ctx: Ctx) -> None:
        ctx.send(sticker_id=ctx.message.sticker.id)

    def on_event_message_text(self, ctx: Ctx) -> None:
        ctx.send(text=ctx.message.text.body)

    def on_event_message_video(self, ctx: Ctx) -> None:
        ctx.send(video_id=ctx.message.video.id, caption=ctx.message.video.caption)
