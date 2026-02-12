This project is a simple and structured Binance Futures Trading Bot built using Python 3 and the python-binance library. 
The bot connects to the Binance USDT-M Futures Testnet and allows users to place BUY/SELL MARKET and LIMIT orders via a command-line interface (CLI).
The steps to run the bot 
  Install dependencies -pip install -r requirements
  configure API - API_KEY ="YOUR_TESTNET_API_KEY"
                  API_SECRET="YOUR_TESTNET_SECRET_KEY"
                  BASE URL ="https://testnet.binancefuture.com"
To Run 
Market Order ex. - python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
Limit sell ex. - python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000

Output - application print -order request summary
                            order response detail
                            success or failiure text
All API request ,responses and errors in bot.log.
