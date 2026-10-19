# Travel Fare Calculator
FARE_RATE = 14

# Validation for passenger name
while True:
    name = input("Enter passenger name: ").strip()
    if name:
        break
    print("Error: Passenger name shouldn't be empty. Please try again.")

# Validation for Distance
while True:
    try:
        distance = float(input("Enter distance (in km): "))
        if distance > 0:
            break
        print("Error: Distance must be greater than 0.")
    except ValueError:
        print("Error: Please enter a valid number for distance.")

# Validation for Passengers
while True:
    try:
        passengers = int(input("Enter number of passengers: "))
        if passengers > 0:
            break
        print("Error: Number of passengers must be positive whole number.")
    except ValueError:
        print("Error: Please enter a valid whole number.")

# Calculate total fare
total_fare = distance * FARE_RATE * passengers

#Display the receipt
print("Passenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
