def main():
    greet = input("Greeting: ")
    print(payout(greet))

def payout(g):
    g = g.strip().lower()
    if g.startswith("hello"):
        return "$0"
    elif g.startswith("h"):
        return "$20"
    else:
        return "$100"


main()