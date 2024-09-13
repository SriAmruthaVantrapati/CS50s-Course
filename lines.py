import sys


def main():

    # checks if the command-line argument is correct
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # checks if command-line argument is a python file
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    # open file argument and trigger error if file does not exist
    try:
        with open(sys.argv[1], "r") as file:
            # creat a list called lines that contains each line from file
            lines = file.readlines()

            # loop updating list to only select each line that does not starts with '#'
            lines = [line for line in lines if not line.strip().startswith("#")]
            # now loop update again list to only select each line that is not whitespace
            lines = [line for line in lines if line.strip() != ""]

            # count each line in the list lines
            print(len(lines))

    except FileNotFoundError:
        # error if file does not exist
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
