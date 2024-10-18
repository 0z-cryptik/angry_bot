from dotenv import load_dotenv
import os
import aiohttp

load_dotenv()

bot_key = os.getenv("BOT_KEY")
url = f"https://api.telegram.org/bot{bot_key}/sendMessage"


async def reply_text(chat_id: str, text: str):
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            if response.status != 200:
                print(f"Failed to send message. error response: {response.status}")
