# ip address #.#.#.# #=0-255
# validate ip address and return True or False

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.match(r"^([0-1]?[0-9]?[0-9]|[2][0-4][0-9]|[2][5][0-5])\.([0-1]?[0-9]?[0-9]|[2][0-4][0-9]|[2][5][0-5])\.([0-1]?[0-9]?[0-9]|[2][0-4][0-9]|[2][5][0-5])\.([0-1]?[0-9]?[0-9]|[2][0-4][0-9]|[2][5][0-5])$", ip):
        return True
    else:
        return False



if __name__ == "__main__":
    main()
