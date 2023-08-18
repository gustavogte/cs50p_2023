import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if search:= re.search(r"(<iframe .*https?://w?w?w?.?youtube.com/embed/)([a-z_A-Z_0-9]+)", s, re.IGNORECASE):
        return f"https://youtu.be/{search[2]}"
    else:
        return None


if __name__ == "__main__":
    main()
