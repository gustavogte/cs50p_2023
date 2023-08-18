def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
       # check for 0 and numbers not in the middle
        for char in s:
            if char.isdigit():
                # creamos un indice para este substring que comienza con un número
                index = s.index(char)
                # Tomamos un slice y checamos que sean solo números juntos y que el útlimo no sea 0
                if s[index:].isdigit() and int(char) != 0:
                    return True
                else:
                    return False
        return True

main()