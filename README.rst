==================
WhatsApp Messenger
==================

.. raw:: html

   <h1 align="center">
     <a href="https://leandcesar.github.io/wa_me">
       <img src="https://github.com/leandcesar/wa_me/blob/main/docs/logo.png?raw=true"  width="200px" alt="wa_me Logo"/>
     </a>
   </h1>

A modern, easy to use, feature-rich ready API wrapper for `WhatsApp Business Cloud`_ written in Python.


* Documentation: https://leandcesar.github.io/wa_me/
* GitHub: https://github.com/leandcesar/wa_me/
* PyPI: https://pypi.org/project/wa_me/
* Free and open source software: MIT license


Features
--------

* Full `Send Messages`_ Support:

  * text
  * media (audio, documents, images, sticker, and videos)
  * contacts
  * interactive (buttons, list, and products)
  * location
  * templates

* Full `Webhook Notification`_ Parsing Support

Installing
----------

Stable release
~~~~~~~~~~~~~~

To install wa_me, run this command in your terminal:

.. code-block:: console

    $ pip install wa_me

This is the preferred method to install wa_me, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

From sources
~~~~~~~~~~~~

The sources for wa_me can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/leandcesar/wa_me

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/leandcesar/wa_me/tarball/main

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install

Quick Example
-------------

Mirror Bot
~~~~~~~~~~

.. code:: py

    from wa_me import Bot, Ctx

    class MirrorBot(Bot):
        def before_event_message(self, ctx: Ctx):
            ctx.read()

        def on_event_message_audio(self, ctx: Ctx):
            ctx.send_audio(ctx.message.audio.id)

        def on_event_message_document(self, ctx: Ctx):
            ctx.send_document(
                ctx.message.document.id,
                caption=ctx.message.document.caption,
            )

        def on_event_message_image(self, ctx: Ctx):
            ctx.send_image(
                ctx.message.image.id,
                caption=ctx.message.image.caption,
            )

        def on_event_message_location(self, ctx: Ctx):
            ctx.send_location(
                latitude=ctx.message.location.latitude,
                longitude=ctx.message.location.longitude,
                address=ctx.message.location.address,
                name=ctx.message.location.name,
            )

        def on_event_message_sticker(self, ctx: Ctx):
            ctx.send_sticker(ctx.message.sticker.id)

        def on_event_message_text(self, ctx: Ctx):
            ctx.send_text(ctx.message.text.body)

        def on_event_message_video(self, ctx: Ctx):
            ctx.send_video(
                ctx.message.video.id,
                caption=ctx.message.video.caption,
            )

Run using Flask
~~~~~~~~~~~~~~~

.. code:: py

    from flask import Flask, request
    from wa_me import Bot

    app = Flask(__name__)
    bot = Bot()
    bot.start(phone_id="PHONE_ID", token="ACCESS_TOKEN")

    @app.get("/")
    async def ping():
        if request.args.get("hub.verify_token") == "VERIFY_TOKEN":
            return request.args.get("hub.challenge")
        return "Invalid verify token"

    @app.post("/")
    def root():
        data = request.get_json()
        bot.handle(data)
        return "Success"

Run using Fast API
~~~~~~~~~~~~~~~~~~

.. code:: py

    from fastapi import FastAPI, Request
    from wa_me import Bot

    app = FastAPI()
    bot = Bot()
    bot.start(phone_id="PHONE_ID", token="ACCESS_TOKEN")

    @app.get("/")
    async def ping(
        token: str = Query(alias="hub.verify_token"),
        challenge: str = Query(alias="hub.challenge"),
    ):
        if token == VERIFY_TOKEN:
            return challenge
        return "Invalid verify token"

    @app.post("/")
    async def root(request: Request):
        data = await request.json()
        bot.handle(data)
        return "Success"

Useful Links
------------

* `Get Started with the WhatsApp Business Cloud API`_

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.


.. _`WhatsApp Business Cloud`: https://developers.facebook.com/docs/whatsapp/cloud-api
.. _`Send Messages`: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages
.. _`Webhook Notification`: https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/components
.. _`pip`: https://pip.pypa.io
.. _`Python installation guide`: http://docs.python-guide.org/en/latest/starting/installation/
.. _`Github repo`: https://github.com/leandcesar/wa_me
.. _`tarball`: https://github.com/leandcesar/wa_me/tarball/main
.. _`Get Started with the WhatsApp Business Cloud API`: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
