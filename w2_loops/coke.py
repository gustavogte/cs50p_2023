# coke = 50
# coins = 25, 10, 5

def main():
    total = 50
    while total <= 50 and total >= 0:
        coin = int(input("Insert Coin: "))
        if coin not in [25, 10, 5]:
            coin = 0
        else:
            total -= coin
        if total > 0:
            print(f"Amount Due: {total}")
        else:
            print(f"Change Owed: {-total}")
            break

def amount_due(c):
    return 50 - c

main()

