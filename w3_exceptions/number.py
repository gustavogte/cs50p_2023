def main():
    x = get_int("What's x? ")
    print(f"x is {x}")



def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass
            #print("x is not an integer")


main()


