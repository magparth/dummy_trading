from flask import Flask, jsonify
import yfinance as yf
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 

# List of top 50 US stock symbols (you can customize this list)
TOP_50_US_STOCKS = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META", "BRK-B", "JNJ", "V",
    "WMT", "PG", "MA", "UNH", "HD", "DIS", "BAC", "PYPL", "XOM", "VZ",
    "KO", "PEP", "INTC", "CSCO", "CMCSA", "ABT", "CVX", "MRK", "NFLX", "ADBE",
    "CRM", "TMO", "PFE", "ABBV", "ORCL", "ACN", "NKE", "T", "QCOM", "DHR",
    "MDT", "LLY", "COST", "AMD", "UNP", "LOW", "UPS", "IBM", "TXN", "SBUX"
]

@app.route("/stocks", methods=["GET"])
def get_stocks():
    stocks_data = []
    for symbol in TOP_50_US_STOCKS:
        stock = yf.Ticker(symbol)
        stock_info = stock.history(period="1d")
        if not stock_info.empty:
            last_close_price = stock_info["Close"].iloc[-1]
            stocks_data.append({
                "symbol": symbol,
                "name": stock.info.get("longName", symbol),
                "price": last_close_price
            })
    return jsonify(stocks_data)

if __name__ == "__main__":
    app.run(debug=True)