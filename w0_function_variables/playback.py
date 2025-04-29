def main():
    text = input()
    print(slow(text))

def slow(sentence):
    return sentence.replace(" ", "...")


main()

