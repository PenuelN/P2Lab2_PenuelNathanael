# Nathanael Penuel
# 10/6
# P2LAB2
# This program calculates the MPG of vehicles.

# Dictionary
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Vehicle names
keys = vehicle_mpg.keys()

# Display
print(keys)

# Select a vehicle
vehicle = input("Enter a vehicle to see its mpg: ")

# Check if the vehicle is in the dictionary
if vehicle in vehicle_mpg:
    mpg = vehicle_mpg[vehicle]
    print(f"The {vehicle} gets {mpg} mpg.")
    
    # How many miles
    miles = float(input(f"How many miles will you drive the {vehicle}? "))
    
    # Gallons
    gallons_needed = miles / mpg
    
    # Display the gallons of gas needed
    print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
else:
    print("The vehicle is not available.")
