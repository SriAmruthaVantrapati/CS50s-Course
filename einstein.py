def main():
    # Speed of light in meters per second
    c = 300000000  # 300,000,000 m/s

    # Prompt the user for mass in kilograms
    mass = int(input("Please enter the mass in kilograms: "))

    # Calculate the energy using E=mc^2
    energy = mass * c**2

    # Output the result as an integer
    print(f"The equivalent energy is {energy} Joules.")

# Call the main function
if __name__ == "__main__":
    main()
