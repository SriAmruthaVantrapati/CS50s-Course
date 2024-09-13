import datetime

def convert_date(date_str):
    """
    Converts a date string in the format "MM/DD/YYYY" or "Month Day, YYYY" to "YYYY-MM-DD".

    Parameters:
    date_str (str): The date string to convert.

    Returns:
    str: The date in "YYYY-MM-DD" format.
    """
    try:
        # Try parsing the date in "MM/DD/YYYY" format
        if "/" in date_str:
            date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y")
        else:
            # Assume the date is in "Month Day, YYYY" format
            date_obj = datetime.datetime.strptime(date_str, "%B %d, %Y")

        # Return the date in "YYYY-MM-DD" format
        return date_obj.strftime("%Y-%m-%d")

    except ValueError:
        # If the date string is not valid, raise an exception
        raise ValueError("Invalid date format. Please enter a valid date.")

def main():
    while True:
        # Prompt the user for a date
        date_str = input("Enter a date (MM/DD/YYYY or Month Day, YYYY): ").strip()

        try:
            # Try to convert the date
            standardized_date = convert_date(date_str)
            # Output the standardized date
            print(standardized_date)
            break  # Exit the loop once a valid date is provided
        except ValueError as e:
            # If the date is invalid, print the error and prompt again
            print(e)

if __name__ == "__main__":
    main()
