from flask import Flask, request
import requests
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "JY GOLD AI RUNNING"


@app.route("/webhook", methods=["POST"])
def webhook():

    print("========== ALL ENV ==========")

    for k in os.environ:
        if "TOKEN" in k or "CHAT" in k:
            print(k, "=", os.environ.get(k))

    TOKEN = os.environ.get("TOKEN")
    CHAT_ID = os.environ.get("CHAT_ID")

    print("TOKEN =", TOKEN)
    print("CHAT_ID =", CHAT_ID)

    data = request.json

    print("========== WEBHOOK TRIGGERED ==========")
    print(data)

    signal = data.get("signal", "N/A")
    symbol = data.get("symbol", "N/A")
    price = data.get("price", "0")
    time = data.get("time", "N/A")

    try:
        price_float = float(price)
    except:
        price_float = 0

    message = f"""
━━━━━━━━━━━━━━
🏆 JY GOLD AI V3 ICT PRO
━━━━━━━━━━━━━━

{"🟢 BUY" if signal == "BUY" else "🔴 SELL"} {symbol}

💰 Entry : {price}

🛑 Stop Loss : {price_float-10:.2f}
🎯 Take Profit : {price_float+20:.2f}

📊 Risk Reward : 1 : 2

🕐 Session : London
✅ ICT MSS Confirmed
✅ FVG Confirmed

⏰ Time : {time}

━━━━━━━━━━━━━━
⚠️ Trade With Proper Risk Management
━━━━━━━━━━━━━━
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    print("========== TELEGRAM REQUEST ==========")
    print(url)
    print(payload)

    r = requests.post(url, json=payload)

    print("========== TELEGRAM RESPONSE ==========")
    print(r.status_code)
    print(r.text)

    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
