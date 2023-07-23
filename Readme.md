# Bus Seat Tracker

The Bus Seat Tracker is a simple Python program that helps you keep track of the number of empty seats on a bus at every stop. It allows you to enter the total number of seats on the bus and then iteratively asks for the number of people who left and boarded the bus at each stop. The program then calculates and displays the number of empty seats at each stop.

## Requirements

- Python 3.x

## How to Use

1. Clone or download the project to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the `bus_seat_tracker.py` file using Python:

   ```
   python bus_seat_tracker.py
   ```

4. The program will prompt you to enter the total number of seats on the bus and the total number of stops.

5. For each stop, the program will ask you to enter the number of people who left the bus and the number of people who boarded the bus.

6. After entering the data for all the stops, the program will display the number of empty seats at each stop.

## Sample Input and Output

```
Enter the number of seats on the bus: 50
Enter the number of stops: 5

Stop 1:
Number of people left the bus: 3
Number of people boarded the bus: 8

Stop 2:
Number of people left the bus: 2
Number of people boarded the bus: 5

Stop 3:
Number of people left the bus: 6
Number of people boarded the bus: 4

Stop 4:
Number of people left the bus: 5
Number of people boarded the bus: 10

Stop 5:
Number of people left the bus: 1
Number of people boarded the bus: 3

Number of empty seats at each stop: [55, 60, 58, 57, 59]
```

## Note

- Ensure that you provide valid inputs for the number of seats and stops. Both inputs should be non-negative integers.

- If the number of people who left the bus at a stop exceeds the number of people currently on the bus, the program will treat it as if all passengers left, resulting in 0 empty seats.

- The program will display an error message if you provide invalid inputs for the number of seats and stops.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
