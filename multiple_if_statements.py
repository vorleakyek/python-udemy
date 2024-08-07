# exercise 1
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller ")
	

# exercise 2 
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("even number")
else:
    print("odd number")
	
	
# exercise 3 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is the age?"))
    if age <= 12:
        print("please pay $5.")
    elif age <= 18:
        print("please pay $7.")
    else:
        print("please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")


# exercise 4 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is the age?"))
    if age <= 12:
        bill = 5
        print("please pay $5.")
    elif age <= 18:
        bill = 7
        print("please pay $7.")
    else:
        bill = 12
        print("please pay $12.")

    wants_photo = input("Want a photo? n or y ")
    if wants_photo == "y":
        bill += 3

    print(f"Final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
