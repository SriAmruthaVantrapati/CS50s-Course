def main():
    time = input("Enter time in HH:MM format: ")
    try:
        c_time = convert(time)
        if 7 <= c_time < 9:
            print("breakfast time")
        elif 12 <= c_time < 14:
            print("lunch time")
        elif 18 <= c_time < 20:
            print("dinner time")
        else:
            print("It's not mealtime.")
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM format.")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours) + (float(minutes) / 60)
    return hours

if __name__ == "__main__":
    main()
