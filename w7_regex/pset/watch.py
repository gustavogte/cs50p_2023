import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if search:= re.findall(r"(<iframe .*https?://w?w?w?.?youtube.com/embed/)([a-z_A-Z_0-9]+)", s, re.IGNORECASE):
        url = search[0]
        return f"https://youtu.be/{url[1]}"
    else:
        return None


if __name__ == "__main__":
    main()