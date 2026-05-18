import requests
from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "supportai"

ACCESS_TOKEN = "EAAOrnFcpWz8BRXDRNmXtE1WI236lQi85FZByYzDMmQZB6oDkXEbJfyU5d00TGR4gjCmHYR2iZCK6Q8Yx9cEWLpcKXYCvULVkaBzhH4ZBz6gqoKMtZCB3dqs8gV13o8jYUZAvUMpFZB3ZCbe9aZBR0b9tzukvFwOIfRN0liFuHDEiknnVRNNtjNMkV90ZAe5h4jpVi5CqLvg5R8ZAh5gwCN719KBgc4rZCn59suifQHMfMzy6u1FZCjK5VkCThwV34jZAUmisW2Whq5S5OPZBETvknDTxTwG7LndTPbvlPrGDwZDZD"

PHONE_NUMBER_ID = "1238581532660962"


@app.route("/")
def home():
    return "Bot funcionando correctamente"


@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    if request.method == "GET":

        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token == VERIFY_TOKEN:
            return challenge

        return "Token incorrecto", 403

    if request.method == "POST":

        data = request.json
        print(data)

        try:
            message = data["entry"][0]["changes"][0]["value"]["messages"][0]
            from_number = message["from"]
            text = message["text"]["body"]

            send_message(from_number, f"Recibí tu mensaje: {text}")

        except:
            pass

        return "ok", 200


def send_message(to, text):

    url = f"https://graph.facebook.com/v25.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text},
    }

    requests.post(url, headers=headers, json=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
