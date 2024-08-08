# Exercise 1
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(max(student_scores))

max = 0
for score in student_scores:
    if score > max:
        max = score

print(max)


# Exercise 2
# range needs to be used together with the for loop; it won't do anything by itself
sum = 0
for number in range(1, 101):
    sum += number
print(sum)


# Exercise 3 
for num in range(1,101):
    if(num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
       
	   
# Exercise 4
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

char_list = []

for letter in range(0, nr_letters):
    char_list.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    char_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
    char_list.append(random.choice(numbers))

print(char_list)

pw = ""
for char in char_list:
    pw += char

print(f"Your password is: {pw}")

random.shuffle(char_list)
random_pw = ""
for char in char_list:
    random_pw += char
print(f"Your password is: {random_pw}")







