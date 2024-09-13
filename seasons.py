from datetime import date
import sys
import inflect

def main():
    seasons_of_love = calculate_words(input("Date of Birth: "))
    print(seasons_of_love.capitalize(), "minutes")


def calculate_words(n):
    try:
        year, month, day = n.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        birthday = date(year, month, day)

        today = date.today()

        time_to_birthday = abs(birthday - today)

        days = time_to_birthday.days
        minutes = days * 24 * 60
        p = inflect.engine()
        words = p.number_to_words(minutes, andword="")
        return words

    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()

