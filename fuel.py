def calculate_fuel_percentage(fraction):
    try:
        numerator, denominator = map(int, fraction.split('/'))

        if denominator == 0 or numerator > denominator:
            raise ValueError

        percentage = numerator / denominator * 100

        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return str(round(percentage))
    except (ValueError, ZeroDivisionError):
        return None

def main():
    while True:
        fraction = input("Enter the fuel fraction (in X/Y format): ")
        percentage = calculate_fuel_percentage(fraction)
        if percentage is not None:
            break
        print("Invalid input. Please try again.")

    print("Fuel percentage:", percentage)

if __name__ == "__main__":
    main()
