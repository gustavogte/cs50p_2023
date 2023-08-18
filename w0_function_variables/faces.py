# Implement main function that prompts the user for input
def main():
    text = input()
    print(convert(text))

def convert(s):
    return s.replace(":)","🙂").replace(":(","🙁")

main()
