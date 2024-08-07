# Tip calculator 

# the input from the users will be a string, so we need to convert it to a number to calculate
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
individual_bill = round((bill / people) * (1 + tip / 100), 2)
print(f"Each person should pay: ${individual_bill:.2f}")

