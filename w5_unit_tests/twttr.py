def main():
    text = input("Input: ")
    print(shorten(text))



def shorten(word):
    vowels = ["A", "E" "I", "O", "U", "a", "e", "i", "o", "u"]
    new_word = ""
    for letter in word:
        if letter in vowels:
            letter = ""
        else:
            letter = letter
            new_word = new_word + letter
    return new_word


if __name__ == "__main__":
    main()