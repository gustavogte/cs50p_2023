from validator_collection import checkers

def main():
    email = input("What's your email address? ")
    print(validate_email(email))


def validate_email(mail):
    if checkers.is_email(mail):
        return "Valid"
    else:
        return "Invalid"

# Other way
"""
def validate_email(email):
    try:
        email_v = validators.email(email)
        if email_v == email:
            return "Valid"
    except ValueError:
        return "Invalid"
"""

if __name__ == "__main__":
    main()






