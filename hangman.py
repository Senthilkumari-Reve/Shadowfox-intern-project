#Implement the wordguessing game with visual progress and hints.
 
import random

# List of possible words
word_list = ["python", "hangman", "developer", "challenge", "shadowfox"]

def choose_word():
    return random.choice(word_list)

def play_hangman():
    word = choose_word()
    guessed = []
    attempts = 6  # Number of wrong guesses allowed

    print("🎮 Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single valid letter.")
            continue

        if guess in guessed:
            print("🔁 You already guessed that letter.")
            continue

        guessed.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            attempts -= 1
            print(f"❌ Wrong! Attempts left: {attempts}")

        # Show current word status
        display = [letter if letter in guessed else "_" for letter in word]
        print(" ".join(display))

        # Check for win
        if "_" not in display:
            print("🎉 Congratulations! You guessed the word.")
            break
    else:
        print(f"💀 Game Over! The word was '{word}'.")

# Play loop
while True:
    play_hangman()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing Hangman!")
        break
