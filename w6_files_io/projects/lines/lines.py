# implement a program which count the lines of python code file
# expects exactly one command-line argument and ends with .py
# else sys.exit()
# don't count lines starting with # orf blank... #

import sys

def main():
    check_file()
    count_lines()

def check_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].strip().endswith(".py") == False:
        sys.exit("Not a Python file")

def count_lines():
    lines = []
    try:
        with open (sys.argv[1]) as file:
            for line in file:
                if line.strip().startswith("#") == False and line.strip() != "":
                    lines.append(line)
        print(len(lines))
    except(FileNotFoundError):
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
