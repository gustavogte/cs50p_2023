import random

# prompt usr for a level n
# if user doesn't input a positive integer => prompt again

def main():
    level = g_level("Level: ")
    r_number = random.randint(1, level)
    #print(r_number)
    guess("Guess: ", r_number)
    print("Just right!")


def g_level(l):
    while True:
        try:
            level = int(input(l))
            if level > 0:
                return level
        except(ValueError):
            pass

def guess(text, r_number):
    while True:
        try:
            g_number = int(input(text))
            if g_number > r_number:
                print("Too large!")
            elif g_number < r_number:
                print("Too small!")
            else:
                break
                # return -1 es igual que break
        except(ValueError):
            pass

if __name__=="__main__":
    main()