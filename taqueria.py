def main():
    # Define the menu with prices
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_cost = 0.0

    try:
        while True:
            # Prompt the user for an item, case-insensitively
            item = input("Enter an item: ").strip().title()

            # Check if the item is on the menu
            if item in menu:
                # Add the price of the item to the total cost
                total_cost += menu[item]

                # Display the total cost formatted to two decimal places
                print(f"Total: ${total_cost:.2f}")
            else:
                # Ignore input that isn't an item on the menu
                continue

    except EOFError:
        # Handle EOF (Control-D) to end input
        print("\nOrder complete.")
        print(f"Final Total: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
