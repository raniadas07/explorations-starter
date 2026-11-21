"""
words.py
Module manages vocabulary data: stores word according to 3 difficulty levels, randomly select a secret word and checks the validity of the word that user types in.
"""

# Define 3 difficulty of 5-letter words: EASY_WORDS, MEDIUM_WORDS, HARD_WORDS
# import random
# import 3 word_list.txt files, split and store them as lists

def load_word_bank(difficulty):
    """Return the word list matching the selected difficulty level."""
    # Step 1: Check if difficulty is 'easy', 'medium', or 'hard'
    # Step 2: Return the corresponding 5-letter word list
    pass


def get_secret_word(word_list):
    """Randomly select one 5-letter word from the word bank."""
    # Step 1: Use random.choice() to pick one word from word_list
    # Step 2: Convert the word to uppercase and return it
    pass


def is_valid_guess(guess):
    """Check if the player's guess is a valid 5-letter alphabetic word."""
    # Step 1: Clean whitespace and convert guess to uppercase
    # Step 2: Check if the length is exactly 5 characters and all characters are letters (A-Z)
    # Step 3: Return True if valid, False otherwise
    pass