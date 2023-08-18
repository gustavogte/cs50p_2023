def main():
    expression = input("Expression: ")
    print(calc(expression))

def calc(e):
    x, y, z  = e.split(" ")
    if y == "+":
        return float(x) + float (z)
    elif y == "-":
        return float(x) - float(z)
    elif y == "*":
        return float(x) * float(z)
    elif y == "/":
        return float(x) / float(z)
main()