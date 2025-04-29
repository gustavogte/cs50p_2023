# omitt vowels (A,E,I,O,U)

""" Easy Way

tweet = input("Input: ")
for letter in tweet:
    if letter not in ["a","e","i","o","u","A","E","I","O","U"]:
        print(letter, end="")
    else:
        print("", end="")
print()
"""


def main():
    text = input("Input: ")
    print(eliminate_vow(text))



def eliminate_vow(text):
    vowels = ["A", "E" "I", "O", "U", "a", "e", "i", "o", "u"]
    new_word = ""
    for letter in text:
        if letter in vowels:
            letter = ""
        else:
            letter = letter
            new_word = new_word + letter
    return new_word

main()