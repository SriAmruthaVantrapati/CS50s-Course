def main():
    # Prompt the user for a greeting
    greeting = input("Greeting: ")
    value=value(greeting)
    print("$" + value)
def value(greeting):
    greeting=greeting.lower().strip()
    if greeting[:5]=="hello":
        return 0
    elif greeting[0]=='h':
        return 20
    else:
        return 100

# Call the main function
if __name__ == "__main__":
    main()

