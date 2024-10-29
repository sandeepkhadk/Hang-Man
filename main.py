import random
from wordl import word  # Import word list from wordl.py
from art import logo, stages  # Import logo and stages from art.py

# Game setup
chosen_word = random.choice(word)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Display game logo
print(logo)

# Create blanks to represent the chosen word
display = ["_" for _ in range(word_length)]

# Main game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")

    # Update display with correctly guessed letters
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If guess is incorrect, reduce lives and notify player
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Display current state of the guessed word
    print(f"{' '.join(display)}")

    # Check if the player has won
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Display remaining lives visually
    print(stages[lives])
