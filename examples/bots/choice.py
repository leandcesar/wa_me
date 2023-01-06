from wa_me import Bot, Ctx
from wa_me.classes.enums import InteractiveType

__all__ = ("ChoiceBot",)


class ChoiceBot(Bot):
    def on_event_message_text(self, ctx: Ctx) -> None:
        alternatives = ctx.message.text.body.title().split()
        if any([len(alternative) > 20 for alternative in alternatives]):
            ctx.send_text(content="Maximum characters per option is 20", mention=True)
        elif 1 <= len(alternatives) <= 3:
            quick_replies = [
                {"id": i, "title": alternative}
                for i, alternative in enumerate(alternatives)
            ]
            ctx.send_quick_replies(
                text="Choose one of the options",
                quick_replies=quick_replies,
                mention=True,
            )
        elif 4 <= len(alternatives) <= 10:
            options = [
                {"id": i, "title": alternative}
                for i, alternative in enumerate(alternatives)
            ]
            ctx.send_options(
                text="Choose one of the options",
                options=options,
                button="Click here",
                title="Options",
                mention=True,
            )
        else:
            ctx.send_text(
                content=f"Maximum options is 10, got {len(alternatives)}",
                mention=True,
            )

    def on_event_message_interactive(self, ctx: Ctx) -> None:
        if ctx.message.interactive.type == InteractiveType.button_reply:
            title = ctx.message.interactive.button_reply.title
            ctx.send_text(content=f"You choose {title!r}", mention=True)
        elif ctx.message.interactive.type == InteractiveType.list_reply:
            title = ctx.message.interactive.list_reply.title
            ctx.send_text(content=f"You choose {title!r}", mention=True)
        else:
            return None
