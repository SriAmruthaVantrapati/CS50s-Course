def main():
    # Prompt the user for the answer
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    # Check if the answer is 42 or any valid string representation of 42
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")
# Call the main function
if __name__ == "__main__":
    main()
