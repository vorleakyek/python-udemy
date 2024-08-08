import random

# Exercise 1

# This will produce a random whole number between 1 and 10 (inclusive).
rand_num = random.randint(1, 10)

# You can generate a random number between 0 (not inclusive) and 1 (inclusive)
# 0.0 <= random.random() < 1.0
rand_num_0_to_1 = random.random()

# This will generate a random floating point number between 1 and 10.
# a <= random.uniform(a,b) <= b
random_float = random.uniform(1, 10)

random_output = random.randint(0, 1)
if random_output == 1:
    print("Head")
else:
    print("Tail")
	
# Exercise 2
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_index = random.randint(0, 4)
print(friends[random_index])

# Exercise 2 
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# option 1
random_index = random.randint(0, 4)
print(friends[random_index])

# option 2
print(random.choice(friends))


# Exercise 3 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# version 1
# list_of_choices = ['rock', 'paper', 'scissors']
#
# human_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))
# computer_choice = random.choice(list_of_choices)
#
# if human_choice == 0:
#     print(f"You chose: \n {rock}")
#     if computer_choice == 'rock':
#         print(f"Computer chose: \n {rock}")
#         print("It's a tie.")
#     elif computer_choice == 'paper':
#         print(f"Computer chose: \n {paper}")
#         print("Computer won!")
#     else:
#         print(f"Computer chose: \n {scissors}")
#         print("You won!")
# elif human_choice == 1:
#     print(f"You chose: \n {paper}")
#     if computer_choice == 'rock':
#         print(f"Computer chose: \n {rock}")
#         print("You won!")
#     elif computer_choice == 'paper':
#         print(f"Computer chose: \n {paper}")
#         print("Tie")
#     else:
#         print(f"Computer chose: \n {scissors}")
#         print("Computer won!")
# elif human_choice == 2:
#     print(f"You chose: \n {scissors}")
#     if computer_choice == 'rock':
#         print(f"Computer chose: \n {rock}")
#         print("Computer won!")
#     elif computer_choice == 'paper':
#         print(f"Computer chose: \n {paper}")
#         print("You won!")
#     else:
#         print(f"Computer chose: \n {scissors}")
#         print("Tie")
# else:
#     print("Please enter 0, 1, or 2.")


# Version 2
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

comp_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[comp_choice])

if user_choice >= 3 or user_choice < 0:
    print("Invalid number.")
elif user_choice == 0 and comp_choice == 2:
    print("You win.")
elif comp_choice == 0 and user_choice == 2:
    print("You lose.")
elif comp_choice > user_choice:
    print("You lose.")
elif user_choice > comp_choice:
    print("You win.")
elif comp_choice == user_choice:
    print("It's a draw!")
