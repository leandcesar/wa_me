from whatsapp import Bot, Ctx
from whatsapp.classes.enums import InteractiveType
from whatsapp.classes.events import Interactive, Text

__all__ = ("ChoiceBot",)


class ChoiceBot(Bot):

    def on_event_message_text(self, ctx: Ctx) -> None:
        alternatives = ctx.message.text.body.title().split()
        if any([len(alternative) > 20 for alternative in alternatives]):
            ctx.reply(text="Maximum characters per option is 20")
        elif 1 <= len(alternatives) <= 3:
            quick_replies = [{"id": i, "title": alternative} for i, alternative in enumerate(alternatives)]
            ctx.reply(text="Choose one of the options", quick_replies=quick_replies)
        elif 4 <= len(alternatives) <= 10:
            options = [{"id": i, "title": alternative} for i, alternative in enumerate(alternatives)]
            ctx.reply(text="Choose one of the options", button="Click here", title="Options", options=options)
        else:
            ctx.reply(text=f"Maximum options is 10, got {len(alternatives)}")

    def on_event_message_interactive(self, ctx: Ctx) -> None:
        if ctx.message.interactive.type == InteractiveType.button_reply:
            ctx.reply(text=f"You choose {ctx.message.interactive.button_reply.title!r}")
        elif ctx.message.interactive.type == InteractiveType.list_reply:
            ctx.reply(text=f"You choose {ctx.message.interactive.list_reply.title!r}")
        else:
            return None
