import argparse
from client import BinanceFuturesClient

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    if args.type == "LIMIT" and args.price is None:
        raise ValueError("Price is required for LIMIT orders")

    client = BinanceFuturesClient()

    print("\n Order Summary")
    print(f"Symbol   : {args.symbol}")
    print(f"Side     : {args.side}")
    print(f"Type     : {args.type}")
    print(f"Quantity : {args.quantity}")
    if args.price:
        print(f"Price    : {args.price}")

    try:
        order = client.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n Order Placed Successfully")
        print(f"Order ID     : {order.get('orderId')}")
        print(f"Status       : {order.get('status')}")
        print(f"Executed Qty : {order.get('executedQty')}")
        print(f"Avg Price    : {order.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("\n Order Failed")
        print("Reason:", e)

if __name__ == "__main__":
    main()

