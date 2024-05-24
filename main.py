def calculate_empty_seats(total_seats, stops):
    empty_seats = total_seats
    empty_seats_at_stops = []

    for stop in range(stops):
        print(f"Stop {stop + 1}:")
        while True:
            try:
                left_at_stop = int(input("Number of people left the bus: "))
                boarded_at_stop = int(input("Number of people boarded the bus: "))

                if left_at_stop < 0 or boarded_at_stop < 0:
                    print("Number of people cannot be negative. Please enter again.")
                    continue

                # Update the number of empty seats
                empty_seats += left_at_stop
                empty_seats -= boarded_at_stop

                # Ensure empty_seats do not exceed total_seats or fall below zero
                empty_seats = max(0, min(empty_seats, total_seats))

                empty_seats_at_stops.append(empty_seats)
                break  # Exit the while loop if inputs are valid
            except ValueError:
                print("Invalid input. Please enter valid integers.")
                continue

    return empty_seats_at_stops

def main():
    try:
        total_seats = int(input("Enter the number of seats on the bus: "))
        stops = int(input("Enter the number of stops: "))

        if total_seats < 0 or stops < 0:
            print("Invalid input. Number of seats and stops must be non-negative.")
            return

        result = calculate_empty_seats(total_seats, stops)
        print("Number of empty seats at each stop:", result)

    except ValueError:
        print("Invalid input. Please enter valid integers for seats and stops.")

if __name__ == "__main__":
    main()
