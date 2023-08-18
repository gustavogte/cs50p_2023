camel = input("camelCase: ")

for letter in camel:
    if letter.isupper():
        letter = "_" + letter.lower()
    print(letter, end="")
print()