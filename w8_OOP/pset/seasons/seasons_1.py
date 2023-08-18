# GG
import sys
import inflect
from datetime import date

def main():
    try:
        input_date = input("Date of Birth: ").split("-")
        input_date = date(int(input_date[0]), int(input_date[1]), int(input_date[2]))
    except(ValueError, IndexError):
        sys.exit("Invalid date")

    print(count_minutes(input_date))

def count_minutes(input_date):
    today = date.today()
    dif = today - input_date

    p = inflect.engine()
    
    minutes = p.number_to_words(int(dif.total_seconds()/60), andword="")
    return f"{minutes.capitalize()} minutes"


if __name__ == "__main__":
    main()