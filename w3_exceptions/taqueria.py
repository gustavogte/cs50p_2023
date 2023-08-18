# When the users input ctrl-d (catch an EOFError) finish order
# After each item input display the total cost with format $0.00
# User input should be case insensitive
# Be sure to catch KeyError

menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

def main():
    # prompt users for items in the menu one per line
    total = 0
    while True:
        try:
            item = input("Item: ")
            if item.title() in menu:
                total += menu[item.title()]
                print(f"Total ${total:.2f}")
        except EOFError:
            print()
            break



main()


