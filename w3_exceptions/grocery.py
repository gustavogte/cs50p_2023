def main():
    cesta()

def cesta():
    cesta = {}
    while True:
        try:
            item = input().upper()
            if item in cesta:
                cesta[item] += 1
            else:
                cesta[item] = 1
        except EOFError:
            break
    for item in sorted(cesta):
        print(cesta[item], item)

main()