def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60

def main():
    user_input = input("Enter the time (in 24-hour format, e.g., 7:30): ")
    time = convert(user_input)

    if 7.0 <= time <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= time <= 13.0:
        print("It's lunch time!")
    elif 18.0 <= time <= 19.0:
        print("It's dinner time!")

if __name__ == "__main__":
    main()
