def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # max 6 characters letters o numbers
    # min 2 charactes
    if len(s) < 2 or len(s) > 6:
        return False

    # plates must start with two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # numbers cannot be in the middle of the plate, must come at the end
    # AAA222 ok AAA22A no ok
    # first number cannot be 0
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1

    # no punctuations marks
    for c in s:
        if c in [".", " ", "!", "?"]:
            return False

    # if all test pass, return True
    return True


main()