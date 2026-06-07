from flask import Flask, request
import requests

app = Flask(__name__)

import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    signal = data.get("signal", "N/A")
    symbol = data.get("symbol", "N/A")
    price = data.get("price", "0")
    time = data.get("time", "N/A")

    message = f"""
━━━━━━━━━━━━━━
🏆 JY GOLD AI V3 ICT PRO
━━━━━━━━━━━━━━

{"🟢 BUY" if signal == "BUY" else "🔴 SELL"} {symbol}

💰 Entry : {price}

🛑 Stop Loss : {float(price)-10:.2f}
🎯 Take Profit : {float(price)+20:.2f}

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

    requests.post(url, json=payload)

    return "OK"

if __name__ == "__main__":
    app.run(port=5000)
