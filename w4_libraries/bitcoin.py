import sys
import requests


def main():
    amount = get_amount()
    bitcoin_rate = get_bitIndex()
    total = amount * bitcoin_rate
    print(f"${total:,.4f}")

def get_amount():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Command-line argument is not a number")
    else:
        try:
            amount = float(sys.argv[1])
            return amount
        except ValueError:
            sys.exit("Command-line argument is not a number")

def get_bitIndex():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/"
        + "currentprice"
        + ".json")
        o = response.json()
        rate = float(o['bpi']['USD']['rate'].replace(",",""))
        return rate
    except requests.RequestException:
        print("Not found")

if __name__ == "__main__":
    main()
