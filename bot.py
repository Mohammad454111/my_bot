import os
import time
import requests

TOKEN = os.environ["BOT_TOKEN"]
API = f"https://api.telegram.org/bot{TOKEN}"

offset = 0

while True:
    response = requests.get(
        f"{API}/getUpdates",
        params={"offset": offset, "timeout": 30}
    )

    data = response.json()

    for update in data.get("result", []):
        offset = update["update_id"] + 1

        message = update.get("message")
        if not message:
            continue

        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            reply = "سلام 👋 ربات با موفقیت فعاله!"
        elif text == "سلام":
            reply = "سلام! 👋 من فعالم."
        else:
            reply = f"پیامت رو دریافت کردم: {text}"

        requests.post(
            f"{API}/sendMessage",
            data={
                "chat_id": chat_id,
                "text": reply
            }
        )

    time.sleep(1)
