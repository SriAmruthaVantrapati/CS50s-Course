import sys
import csv
from tabulate import tabulate


def main():
    # checks if the command-line argument is correct
    file_open(sys.argv)

    # create an empty list
    csv_list = []
    # try to open command-line argument and trigger error if file does not exist
    try:
        with open(sys.argv[1], "r") as file:
            # read CSV file
            csv_content = csv.reader(file)
            # read the first row as header
            header_row = next(csv_content)
            for row in csv_content:
                csv_list.append(row)

            print(tabulate(csv_list, headers=header_row, tablefmt="grid"))

    except FileNotFoundError:
        # error if file does not exist
        sys.exit("File does not exist")

def file_open(v):
    # checks if no command-line argument
    if len(v) < 2:
        sys.exit("Too few command-line arguments")
    # checks if to many command-line argument
    if len(v) > 2:
        sys.exit("Too many command-line arguments")
    # checks if command-line argument is a CSV file
    if not v[1].strip().endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
