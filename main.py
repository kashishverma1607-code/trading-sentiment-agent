from src.config import ASSETS


def main():

    print("=" * 60)
    print("TRADING SENTIMENT PRICE PREDICTION AGENT")
    print("=" * 60)

    total_assets = 0

    for exchange, stocks in ASSETS.items():

        print(f"\nExchange: {exchange}")
        print("-" * 60)

        for stock in stocks:

            print(
                f"{stock['ticker']} | "
                f"{stock['name']} | "
                f"{stock['currency']}"
            )

            total_assets += 1

    print("\n" + "=" * 60)
    print(f"Total exchanges: {len(ASSETS)}")
    print(f"Total stocks: {total_assets}")
    print("Configuration loaded successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
