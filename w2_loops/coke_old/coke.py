def main():
    amount = 50
    print(f"Amount Due: {amount}")
    while amount > 0:
        coin = int(input("Insert Coin: "))
        coin = check_coin(coin)
        amount = amount - coin
        if amount <= 0:
            print("Change Owed:", -amount)
            break
        print("Amount Due:", amount)

def check_coin(c):
    if c == 25:
        return 25
    elif c == 10:
        return 10
    elif c == 5:
        return 5
    else:
        return 0

main()
