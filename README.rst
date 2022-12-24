===========
whatsapp-py
===========


.. image:: https://img.shields.io/pypi/v/whatsapp.svg
    :target: https://pypi.python.org/pypi/whatsapp

.. image:: https://img.shields.io/travis/leandcesar/whatsapp.svg
    :target: https://travis-ci.com/leandcesar/whatsapp

.. image:: https://readthedocs.org/projects/whatsapp/badge/?version=latest
    :target: https://whatsapp.readthedocs.io/en/latest/?version=latest
    :alt: Documentation Status

.. image:: https://pyup.io/repos/github/leandcesar/whatsapp/shield.svg
     :target: https://pyup.io/repos/github/leandcesar/whatsapp/
     :alt: Updates

.. raw:: html

   <h1 align="center">
   <a href="https://leandcesar.github.io/whatsapp/"><img src="docs/logo.png" width="200px" alt="whatsapp-py"></a>
   </h1>
   

A modern, easy to use, feature-rich ready API wrapper for `WhatsApp Business Cloud`_ written in Python.


* Documentation: https://leandcesar.github.io/whatsapp/
* GitHub: https://github.com/leandcesar/whatsapp/
* PyPI: https://pypi.org/project/whatsapp-py/
* Free and open source software: MIT license


Features
--------

* Full `Send Messages`_ Support (text, audio, contacts, documents, images, interactive, location, sticker, and videos)
* Full `Webhook Notification`_ Parsing Support

Installing
----------

To install whatsapp-py, run this command in your terminal:

.. code-block:: console

    $ pip install whatsapp

This is the preferred method to install whatsapp-py, as it will always install
the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

Quick Example
-------------

Mirror Bot
~~~~~~~~~~

.. code:: py

    from whatsapp import Bot, Ctx

    class MirrorBot(Bot):
        def before_event_message(self, ctx: Ctx):
            ctx.read()

        def on_event_message_audio(self, ctx: Ctx):
            ctx.send(audio_id=ctx.message.audio.id)

        def on_event_message_document(self, ctx: Ctx):
            ctx.send(document_id=ctx.message.document.id, caption=ctx.message.document.caption)

        def on_event_message_image(self, ctx: Ctx):
            ctx.send(image_id=ctx.message.image.id, caption=ctx.message.image.caption)

        def on_event_message_sticker(self, ctx: Ctx):
            ctx.send(sticker_id=ctx.message.sticker.id)

        def on_event_message_text(self, ctx: Ctx):
            ctx.send(text=ctx.message.text.body)

        def on_event_message_video(self, ctx: Ctx):
            ctx.send(video_id=ctx.message.video.id, caption=ctx.message.video.caption)

Run using Flask
~~~~~~~~~~~

.. code:: py

    from flask import Flask, request
    from whatsapp import Bot

    app = Flask(__name__)
    bot = Bot()
    bot.start(phone_id="YOUR_PHONE_ID", token="YOUR_ACCESS_TOKEN")

    @app.get("/")
    async def ping():
        if request.args.get("hub.verify_token") == "YOUR_VERIFY_TOKEN":
            return request.args.get("hub.challenge")
        return "Invalid verify token"

    @app.post("/")
    def root():
        data = request.get_json()
        bot.handle(data)
        return "Success"

Run using Fast API
~~~~~~~~~~~~~~

.. code:: py

    from fastapi import FastAPI, Request
    from whatsapp import Bot

    app = FastAPI()
    bot = Bot()
    bot.start(phone_id="YOUR_PHONE_ID", token="YOUR_ACCESS_TOKEN")

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


.. _WhatsApp Business Cloud: https://developers.facebook.com/docs/whatsapp/cloud-api
.. _Send Messages: https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages
.. _Webhook Notification: https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/components
.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/
.. _Get Started with the WhatsApp Business Cloud API: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _audreyr/cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
