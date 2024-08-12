# My Version 
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

counter = 0
remaining_letters = word_length
display_list = list(placeholder)
isUpdate = True

while counter < 7 and remaining_letters > 0:
    isUpdate = True
    guess = input("Guess a letter: ").lower()
    number_correct_letters_guessed = 0

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display_list[index] = letter
            number_correct_letters_guessed += 1
            isUpdate = False

    display_str = "".join(display_list)

    if isUpdate:
        counter += 1

    remaining_letters -= number_correct_letters_guessed
    print(f"counter: {counter}")
    print(f"remaining_letters: {remaining_letters}")
    print(display_str)


print("Play again! ")


# Solution: 
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
  placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
  guess = input("Guess a letter: ").lower()

  display = ""

  for letter in chosen_word:
      if letter == guess:
          display += letter
          correct_letters.append(guess)
      elif letter in correct_letters:
          display += letter
      else:
          display += "_"

  print(display)

  if "_" not in display:
      game_over = True
      print("You win.")


# Final version solution 
import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])


