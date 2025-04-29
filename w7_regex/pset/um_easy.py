import re


def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"\b\W*um\W", s, re.IGNORECASE)
    return len(um)


if __name__ == "__main__":
    main()