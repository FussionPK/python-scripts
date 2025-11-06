import math

try:
    # Collecting temperatures from user input and writing to the file
    for i in range(1, 6):
        user = float(input("Please input a temperature: "))
        with open("temps.txt", "a") as fappend:
            fappend.write(f"Day {i}: {user}\n")

    # Reading temperatures from the file
    with open("temps.txt", "r") as fread:
        lines = fread.readlines()  # Read all lines into a list

    # Extracting temperature values using list comprehension
    temperatures = [
        float(line.split(":")[1].strip()) if line else None
        for line in lines
    ]

    print("Below is the calculation to get the average")

    # Calculating total and average
    total = sum(temperatures)  # Use sum on the list of temperatures
    average = total / len(temperatures) if temperatures else 0  # Avoid division by zero

    print("Total:", total)
    print(f"Average: {average:.2f}")

except:
    print("Execution Error:")
