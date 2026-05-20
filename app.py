import requests
from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "supportai"

ACCESS_TOKEN = "EAAOrnFcpWz8BRpM0va3ZCHBsYZBXb265Kw6bv3aWFZCQEKa5QZBZCSGGNZCYZAN058gI9QnS2vVbyNX9aZBkKDujKakZC5SWZAXZATdU9UPKac3dU5WJdqmWhZAgzsbzLyZAnGTZADe7gl6ZBUZB3dCLMbOOIB6bkAoL19JbCd5hZAzLnxhfcrm0ug0PJE8Q1O5zScOZAzK58UrcXjQMIBBBwAWPKD3B6zFUqbUaDeHmryKoJwCIZCyxcQKHNBnAyN5Sl6OfVJ1Kr4uob2mlAWSIbHC7ohzsdwZA3ztSSR9LccuDRgZDZD"

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
