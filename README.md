**Hangman Game 🎮**
A console-based Python implementation of the classic Hangman game, where players guess letters to reveal a hidden word. This project uses a word list and ASCII art for a fun and interactive experience.

**Features**
•	Random Word Selection: A word is chosen at random for each game from a predefined list.
•	ASCII Art: The game includes visual representations of each stage of the hangman.
•	Lives System: Players have 6 attempts (lives) to guess the word before losing the game.
•	Feedback: The game gives feedback after each guess, showing correct and incorrect guesses and previously guessed letters

**Requirements**
This project uses:
•	Python 3.x
•	Two additional files:
o	wordl.py: Contains a list of words (word) for the game.
o	art.py: Contains ASCII art for the game's logo and hangman stages (logo and stages).

Ensure that both wordl.py and art.py are in the same directory as this script.

**How to Play**
1.	Clone the repository or download all project files.
2.	Ensure you have the required files:
o	main.py (this script)
o	wordl.py (word list)
o	art.py (logo and hangman stages)
4.	Run the script:
python main.py
5.	Guess letters by typing them when prompted. If the letter is in the word, it will appear in the correct position(s). If not, you'll lose a life.
6.	Continue guessing until you either reveal the word or run out of lives.

**Example**
Welcome to Hangman!
Guess a letter: e
_ e _ _ _
Guess a letter: r
You guessed r, that's not in the word. You lose a life.
Lives remaining: 5
Guess a letter: ...

**License**
This project is open-source and free to use for educational purposes.

