# Binance Futures Trading Bot (Testnet)

## Overview
This project is a simple and structured **Binance Futures Trading Bot** built using **Python 3** and the **python-binance** library.

The bot connects to the **Binance USDT-M Futures Testnet** and allows users to place **BUY/SELL MARKET and LIMIT orders** via a **command-line interface (CLI)**.

---

## Features
- Binance Futures Testnet (USDT-M)
- MARKET and LIMIT orders
- BUY and SELL support
- CLI-based input
- Input validation and error handling
- Logging of API requests, responses, and errors

---

## Project Structure
binance_trading_bot/
│
├── main.py 
├── client.py 
├── config.py 
├── bot.log

---

## Setup

### 1. Install dependencies
```bash
pip install python-binance


 2. Configure API key
  API_KEY = "YOUR_TESTNET_API_KEY"
  API_SECRET = "YOUR_TESTNET_SECRET_KEY"
  BASE_URL = "https://testnet.binancefuture.com"


 3. Usage
   Market Order (BUY) - python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
   Limit Order (SELL) - python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000



 4. Output

The application prints:

Order request summary

Order execution result

Success or failure message

All API requests, responses, and errors are logged in bot.log.
