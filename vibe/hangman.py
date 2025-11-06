try:
    with open("words.txt", "r") as fread:
        words = fread.readlines()
        words = [word.strip() for word in words]
        import random
        secret_word = random.choice(words)
        print("The secret word has", len(secret_word), "letters.")
        
        while True:
            guess = input("Guess a word: ").strip().lower()
            if guess == secret_word:
                print("Congratulations! You've guessed the word correctly.")
                break
            elif guess in secret_word:
                print("Good guess! The letter", guess, "is in the word.")
            else:
                print("Incorrect guess. Try again.")
                print("The secret word contains the letter:", random.choice(secret_word))
except Exception as e:
    print("An error occurred:", e)
    print("Please make sure the words.txt file is present and contains valid words.")
    print("Error details:", e)
    print("Exiting the game.")
    exit()
else:
    print("Thank you for playing Hangman!")
finally:
    print("Game session ended.")
