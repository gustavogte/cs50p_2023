# prompt user for a fraction formatted as "X/Y" where X and Y are integers
# output the % rounded to the nearst integer
# 1% or less => E, 99% or more ==> F


def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)


def convert(fraction):
    while True:
        try:
            numerator, denominator = fraction.split(sep="/")
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            f = new_numerator / new_denominator
            if f <= 1:
                p = f * 100
                return int(p)
        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction: ")
            pass
            #raise



def gauge(percentage):
    # print(percentage)
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
