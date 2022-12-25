from wabc import Bot, Ctx
from wabc.utils.routine import routine
from wabc.utils.ttl_dict import TTLDict

__all__ = ("HistoryBot",)


class HistoryBot(Bot):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.chats = TTLDict(max_len=50, ttl=600, reset_on_get=True)

    def before_event(self, ctx: Ctx) -> None:
        if ctx.recipient_id and ctx.recipient_id not in self.chats:
            self.chats[ctx.recipient_id] = TTLDict(max_len=20, reset_on_get=True)

    def before_event_message(self, ctx: Ctx) -> None:
        self.chats[ctx.recipient_id][ctx.message.id] = ctx.message

    def after_event(self, ctx: Ctx) -> None:
        for reply_id, reply in zip(ctx.replies_ids, ctx.replies):
            self.chats[ctx.recipient_id][reply_id] = reply

    def on_event_message_text(self, ctx: Ctx) -> None:
        ctx.send(text=ctx.message.text.body)

    @routine(seconds=60)
    def show_chats(self) -> None:
        for recipient_id, messages in self.chats.items():
            for message_id in messages.keys():
                print(f"{recipient_id}\t{message_id}")
