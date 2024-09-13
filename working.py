import re


def main():
    print(convert(input("Hours: ")))

def convert(s):
    time_comparison = {
        "12 AM": "00",
        "1 AM": "01",
        "2 AM": "02",
        "3 AM": "03",
        "4 AM": "04",
        "5 AM": "05",
        "6 AM": "06",
        "7 AM": "07",
        "8 AM": "08",
        "9 AM": "09",
        "10 AM": "10",
        "11 AM": "11",
        "12 PM": "12",
        "1 PM": "13",
        "2 PM": "14",
        "3 PM": "15",
        "4 PM": "16",
        "5 PM": "17",
        "6 PM": "18",
        "7 PM": "19",
        "8 PM": "20",
        "9 PM": "21",
        "10 PM": "22",
        "11 PM": "23"
}

    s = s.strip()
    p = r"^(\d|1[0-2])(:[0-5][0-9])? (AM|PM) to (\d|1[0-2])(:[0-5][0-9])? (AM|PM)$"
    match = re.search(p, s)

    if match:
        x = f"{match.group(1)} {match.group(3)}"
        y = f"{match.group(4)} {match.group(6)}"
        for times in time_comparison:
            if times == x:
                x = time_comparison[times]
            if times == y:
                y = time_comparison[times]
    else:
        raise ValueError

    if match.group(2) and match.group(5):
        return f"{x}{match.group(2)} to {y}{match.group(5)}"
    if match.group(2):
        return f"{x}{match.group(2)} to {y}:00"
    if match.group(5):
        return f"{x}:00 to {y}{match.group(5)}"
    else:
        return f"{x}:00 to {y}:00"

if __name__ == "__main__":
    main()
