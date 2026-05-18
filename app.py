from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Bot funcionando correctamente"


@app.route("/webhook", methods=["GET", "POST"])
def webhook():

    if request.method == "GET":
        return "Webhook conectado correctamente"

    if request.method == "POST":
        data = request.json
        print(data)

        return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
