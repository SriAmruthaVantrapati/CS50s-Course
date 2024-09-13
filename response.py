import validators

def main():
    print(response(input("What's your email address? ")))


def response(n):

    if validators.email(n):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
