from os import environ

from fastapi import FastAPI, Query, Request

from wa_me import Bot

ACCESS_TOKEN = environ["ACCESS_TOKEN"]
VERIFY_TOKEN = environ["VERIFY_TOKEN"]
PHONE_ID = environ["PHONE_ID"]

app = FastAPI()
bot = Bot()
bot.start(phone_id=PHONE_ID, token=ACCESS_TOKEN)


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
