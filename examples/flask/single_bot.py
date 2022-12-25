from os import environ

from flask import Flask, request

from wa_me import Bot

ACCESS_TOKEN = environ["ACCESS_TOKEN"]
VERIFY_TOKEN = environ["VERIFY_TOKEN"]
PHONE_ID = environ["PHONE_ID"]

app = Flask(__name__)
bot = Bot()
bot.start(phone_id=PHONE_ID, token=ACCESS_TOKEN)


@app.get("/")
def ping():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid verify token"


@app.post("/")
def root():
    data = request.get_json()
    bot.handle(data)
    return "Success"
