def main():
    greeting = input("Greeting: ")
    v = value(greeting)
    print(f"${v:.0f}")

def value(greeting):
    g = greeting.strip().lower()
    if g.startswith("hello"):
        return 0
    elif g.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()