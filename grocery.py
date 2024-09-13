def main():
    # Dictionary to store items and their counts
    grocery = {}
    while True:
        try:
            item = input()
        except EOFError:
            print()
            break
    # Add or update the count of the item in the grocery list
        if item.upper() in grocery:
            grocery[item.upper()] += 1
        else:
            grocery[item.upper()] = 1
        # Sort the items alphabetically and output them in uppercase with counts
    for item in sorted(grocery.keys()):
        print(grocery[item],item)

if __name__ == "__main__":
    main()
