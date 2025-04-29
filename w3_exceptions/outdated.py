months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    month, day, year = get_date("Date: ")
    if month.isalpha():
        month = months.index(month)+1
    print(f"{year}-{int(month):02}-{int(day):02}")

def get_date(prompt):
    while True:
        date = input(prompt)
        # Try first format
        try:
            date = date.strip().split(" ")
            month = date[0]
            day = date[1].strip(",")
            year = date[2]
            if month.title() in months and int(day) > 0 \
                and int(day) <= 31 and len(year) == 4 and int(year) > 0:
                return month.title(), day, year
        except (ValueError, EOFError, IndexError):
            # Try second format
            try:
                # Now date is a list with only one item date[0]
                new_date = date[0].split("/")
                month = new_date[0]
                day = new_date[1]
                year = new_date[2]
                if int(month) > 0 and int(month) <= 12 and int(day) > 0 \
                    and int(day) <= 31 and len(year) == 4 and int(year) > 0:
                    return month, day, year
            except (ValueError, EOFError, IndexError):
                pass



main()