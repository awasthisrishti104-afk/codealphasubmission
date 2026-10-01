import random
def playhangman():
    words = ["python", "codealpha", "developer", "script", "program"]
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    print("Welcome to Hangman!")
    while incorrect_guesses < max_incorrect_guesses:
        display_word = [letter if letter in guessed_letters else '_' for letter in secret_word]
        print("\n Word: " + " ".join(display_word))
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        if '_' not in display_word:
            print(f"\n Congratulations! You guessed the word: {secret_word}")
            break
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one!")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\n Game Over! You got out of guesses. The word was: {secret_word}")
if __name__ == "__main__":
    playhangman()