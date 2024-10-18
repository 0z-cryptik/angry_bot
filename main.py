from telegram.ext import ApplicationBuilder
from dotenv import load_dotenv
import os
from reply_text import reply_text
from roasts import curses_func, emojis
from flask import Flask, request

load_dotenv()

bot_key = os.getenv("BOT_KEY")

bot_url = f"https://api.telegram.org/bot{bot_key}"

app = Flask(__name__)

ApplicationBuilder().token(bot_key).build()


@app.route("/webhook", methods=["POST"])
async def webhook():
    json_data = request.get_json()
    sender_name = json_data["message"]["from"]["first_name"]
    chat_id = json_data["message"]["from"]["id"]
    message = json_data["message"]["text"]
    print(f"message from{sender_name}: {message}")
    if message == "/start":
        reply = f"Hi {sender_name}, kindly off {emojis['slightly_smiling_face']}"
    else:
        reply = curses_func(sender_name, message)
    await reply_text(chat_id, reply)
    return "ok"
