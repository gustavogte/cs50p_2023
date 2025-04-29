# from random import choice
# then you don't have to use random.choice(), just choice()

import random

cards = ["jack", "queen", "king"]

random.shuffle(cards)

for card in cards:
    print(card)
print()

number = random.randint(1, 10)
print(f"{number}\n")

coin = ["heads", "tails"]
coin = random.choice(coin)
print(coin)
print()
