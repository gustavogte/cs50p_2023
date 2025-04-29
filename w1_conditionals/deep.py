def main():
    q = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    print(answer(q))

def answer(x):
    x = x.strip().lower()
    match x:
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"

main()
