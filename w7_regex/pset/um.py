import re


def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"um", s, re.IGNORECASE)
    um_w = re.findall(r"\b\wum\b|um\w|\wum", s, re.IGNORECASE)
    #print(um, um_w)
    return len(um) - len(um_w)


if __name__ == "__main__":
    main()
