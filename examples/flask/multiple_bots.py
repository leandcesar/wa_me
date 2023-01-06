from os import environ

from flask import Flask, request

from whatsapp import Bot, TTLDict

ACCESS_TOKEN = environ["ACCESS_TOKEN"]
VERIFY_TOKEN = environ["VERIFY_TOKEN"]
PHONE_ID = environ["PHONE_ID"]

app = Flask(__name__)
bots: TTLDict = TTLDict(ttl=600, reset_on_get=True)


def get_access_token_from_phone_id(phone_id: str) -> str:
    # TODO: db fetch or something else...
    mock_db = {PHONE_ID: ACCESS_TOKEN}
    return mock_db[phone_id]


def get_or_create_bot_from_phone_id(phone_id: str) -> Bot:
    if phone_id in bots:
        bot = bots[phone_id]
    else:
        token = get_access_token_from_phone_id(phone_id)
        bot = Bot()
        bot.start(phone_id, token)
        bots[phone_id] = bot
    return bot


@app.get("/")
async def ping():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid verify token"


@app.post("/")
def root():
    data = request.get_json()
    phone_id = data["entry"][0]["changes"][0]["value"]["metadata"]["phone_number_id"]
    bot = get_or_create_bot_from_phone_id(phone_id)
    bot.handle(data)
    return "Success"
