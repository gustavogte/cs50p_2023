# Tabulate pizza
# Utilizamos csv reader para crear un lista de las columas, dentro de pizzas[]

import sys
import csv

from tabulate import tabulate

def main():
    check_file()
    get_pizza()


def check_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].strip().endswith(".csv") == False:
        sys.exit("Not a CSV file")


def get_pizza():
    try:
        pizzas = []
        with open (sys.argv[1]) as file:
            reader = csv.reader(file)
            for pizza in reader:
                pizzas.append(pizza)
    except(FileNotFoundError):
        sys.exit("File does not exist")
    #print pizzas List :
    #print(pizzas)
    print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()
