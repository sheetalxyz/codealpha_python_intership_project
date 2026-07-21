import random

# List of words
words = ["python", "apple", "orange", "school", "computer"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("===== HANGMAN GAME =====")

while wrong_guesses < max_wrong_guesses:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if player guessed the whole word
    if "_" not in display:
        print("\nCongratulations! You guessed the word.")
        break

    guess = input("Enter one letter: ").lower()

    # Only one letter is allowed
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check if letter already entered
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Correct or wrong guess
    if guess in word:
        print("Correct Guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")
        print("Remaining Chances:", max_wrong_guesses - wrong_guesses)

# If all chances are over
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The correct word was:", word)