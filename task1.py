import random
import os

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word():
    """Return a random word from a chosen category."""
    categories = {
        'Animals': ['elephant', 'giraffe', 'penguin', 'dolphin', 'kangaroo', 'zebra'],
        'Countries': ['france', 'japan', 'brazil', 'egypt', 'canada', 'india'],
        'Food': ['pizza', 'sushi', 'burger', 'pasta', 'taco', 'sandwich'],
        'Sports': ['soccer', 'tennis', 'basketball', 'volleyball', 'swimming']
    }
    
    print("\nChoose a category:")
    for i, category in enumerate(categories.keys(), 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            choice = int(input("\nEnter category number: "))
            if 1 <= choice <= len(categories):
                category = list(categories.keys())[choice - 1]
                return random.choice(categories[category]), category
        except ValueError:
            pass
        print("Please enter a valid category number!")

def display_game_state(word_display, guessed_letters, attempts, category):
    """Display the current game state."""
    clear_screen()
    print("\n=== HANGMAN ===")
    print(f"\nCategory: {category}")
    print(f"\nWord: {' '.join(word_display)}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Attempts remaining: {attempts}")

def play_hangman():
    """Main game function."""
    print("\n=== Welcome to Hangman! ===")
    print("Try to guess the word one letter at a time.")
    
    word, category = get_word()
    word_display = ['_' for _ in word]
    guessed_letters = set()
    attempts = 6
    
    while attempts > 0:
        display_game_state(word_display, guessed_letters, attempts, category)
        
        guess = input("\nGuess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            input("Please enter a single letter! Press Enter to continue...")
            continue
            
        if guess in guessed_letters:
            input("You already guessed that letter! Press Enter to continue...")
            continue
            
        guessed_letters.add(guess)
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
            if '_' not in word_display:
                display_game_state(word_display, guessed_letters, attempts, category)
                print(f"\nCongratulations! You won! The word was '{word}'!")
                break
        else:
            attempts -= 1
            if attempts == 0:
                display_game_state(word_display, guessed_letters, attempts, category)
                print(f"\nGame Over! The word was '{word}'.")
                break
    
    if input("\nWould you like to play again? (y/n): ").lower() == 'y':
        play_hangman()

if __name__ == "__main__":
    play_hangman()
