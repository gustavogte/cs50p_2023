def main():
    tank = get_tank("Fraction: ")
    if tank <= 0.01:
        print("E")
    elif tank >= 0.99:
        print("F")
    else:
       print(f"{round(tank * 100)}%")

def get_tank(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            if int(x) <= int(y):
                tank = int(x) / int(y)
                return tank
        except (ValueError, ZeroDivisionError):
            pass


main()