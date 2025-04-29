fruits = [
    {"item": "apple", "calories": 130},
    {"item": "avocado", "calories": 50},
    {"item": "banana", "calories": 110},
    {"item": "cantaloupe", "calories": 50},
    {"item": "grapefruit", "calories": 60},
    {"item": "grapes", "calories": 90},
    {"item": "Honeydew Melon", "calories": 80},
    {"item": "Kiwifruit", "calories": 90},
    {"item": "Lemon", "calories": 15},
    {"item": "Lime", "calories": 20},
    {"item": "Nectarine", "calories": 60},
    {"item": "Orange", "calories": 80},
    {"item": "Peach", "calories": 60},
    {"item": "Pineapple", "calories": 100},
    {"item": "Strawberries", "calories": 50},
    {"item": "Sweet Cherries", "calories": 100},
    {"item": "Tangerine", "calories": 50},
    {"item": "Watermelon", "calories": 80},
    {"item": "Pear", "calories": 100},
]

item = input("Item: ")
for fruit in fruits:
    if item.lower() == fruit["item"].lower():
        print(f"Calories: {fruit['calories']}")

