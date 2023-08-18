# Vanity plates
# ok start with at least 2 letters
# ok max 6 char min 2 char
# ok No periods, spaces, or punctuation marks
# numbers must go at the end
# first number must not be a 0
# 
## Input plate by the user
## determine if it is Valid o Invalid
## You can implement one function per requierement on is_valid()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_len(s) and check_begin(s) and s.isalnum() and check_num(s):
        return True

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

main()
