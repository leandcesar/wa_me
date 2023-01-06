from typing import Any, Dict, Union

from wa_me import Bot, Ctx, events, messages

__all__ = ("HistoryBot",)


class HistoryBot(Bot):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._history: Dict[
            str, Dict[str, Union[events.Message, messages.Message]]
        ] = {}

    def before_event(self, ctx: Ctx) -> None:
        if ctx.recipient_id and ctx.recipient_id not in self._history:
            self._history[ctx.recipient_id]: Dict[str, Any] = {}

    def before_event_message(self, ctx: Ctx) -> None:
        self._history[ctx.recipient_id][ctx.message.id] = ctx.message

    def on_event_message_text(self, ctx: Ctx) -> None:
        ctx.send_text(content=ctx.message.text.body)

    def after_event(self, ctx: Ctx) -> None:
        for reply_id, reply in zip(ctx.replies_ids, ctx.replies):
            self._history[ctx.recipient_id][reply_id] = reply

    def print_history(self) -> None:
        for recipient_id, _messages in self._history.items():
            for message_id, message in _messages.items():
                print(f"{recipient_id}\t{message_id}\t{message.text.body}")
