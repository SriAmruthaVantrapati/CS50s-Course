def convert(input_str):
    # Replace :) with 🙂
    converted_str = input_str.replace(":)", "🙂")
    # Replace :( with 🙁
    converted_str = converted_str.replace(":(", "🙁")
    return converted_str
def main():
    # Prompt the user for input
    user_input = input("Please enter a string: ")
    # Convert the input
    converted_input = convert(user_input)
    # Print the result
    print(converted_input)
# Call the main function
if __name__ == "__main__":
    main()
