# pc
from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid date")

    print(minutes_lived(year, month, day))


def minutes_lived(year, month, day):
    try:
        date_b = date(int(year), int(month), int(day))
    except ValueError:
        return sys.exit("Invalid date")
    today = date.today()
    dif_dates = today - date_b
    minutes = int(dif_dates.total_seconds() / 60)
    message = p.number_to_words(minutes, andword="") + " minutes"
    return message.capitalize()


if __name__ == "__main__":
    main()
