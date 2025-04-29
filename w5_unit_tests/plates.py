def main():
    plate = input("Plate: ")
    v = is_valid(plate)
    if v == True:
        print("Valid")
        #print(v)
    else:
        print("Invalid")
        #print(v)


def is_valid(s):
    if check_len(s) and check_begin(s) and s.isalnum() and check_num(s):
        return True
    else:
        return False

def check_len(p):
    if len(p) > 1 and len(p) < 7:
        return True

def check_begin(p):
    if check_len(p) and p[0].isalpha() and p[1].isalpha():
        return True

def check_num(num):
    if num.isalpha():
        return True
    else:
        for char in num:
            if char.isdigit():
                index = num.index(char)
                if num[index:].isdigit() and char != "0":
                    return True
                else:
                    return False

def check_end(p):
    if p[-1:] != "" or p[-1:] != "0":
        return True

if __name__ == "__main__":
    main()