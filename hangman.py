import random

# Function to choose a random word
def choose_word():
    words = ["python", "java", "hangman", "coding", "developer"]
    return random.choice(words)

# Main function to play hangman
def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("🎮 Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("\nEnter a letter: ").lower()

        if guess in guessed_letters:
            print("⚠ You already guessed this letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
        else:
            attempts -= 1
            print("❌ Wrong guess! Attempts left:", attempts)

        # Display current word status
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word)

        # Check win condition
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break

    # Lose condition
    if attempts == 0:
        print("\n💀 Game Over! The word was:", word)

# Call the function
play_hangman()