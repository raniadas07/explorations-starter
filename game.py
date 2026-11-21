"""
game.py
Module handles logic of the game: count number of guess times,
compare each letter to return hints and check the condition of win/lose.
"""

# import is_valid_guess từ words.py and the function display from board.py
# import time (used to measure time from round start to finish)

def get_max_tries(difficulty):
    """Determine how many guesses the player gets based on difficulty."""
    # Return 6 tries if the mode is 'easy', return 5 tries is the mode is 'medium' or 'hard'
    pass


def evaluate_guess(guess, secret_word, difficulty):
    """Compare guess against secret_word and assign tile colors ('GREEN', 'YELLOW', 'GRAY')."""
    # Step 1: Initialize a list of 5 'GRAY' statuses
    # Step 2: First pass - mark exact letter & position matches as 'GREEN'
    # Step 3: Second pass - mark letters in the word but in the wrong spot as 'YELLOW'
    # Step 4: If difficulty is 'hard', convert any 'GREEN' tiles to 'YELLOW' (no exact-spot clue)
    # Step 5: Return the list of 5 color statuses
    pass


def play_round(difficulty, target_word):
    """Run one complete round of Wordle from the first guess to win or loss, track board history,
    and measure time taken from start to finish.
    Return: result, time."""
    # Step 1: Get max_tries and call board.print_game_rules()
    # Step 2: Initialize an empty list `board_history = []` to store (guess, feedback) pairs
    # Step 3: Record `start_time = time.time()` right before the first guess
    # Step 4: Loop through each attempt from 1 up to max_tries:
    #   - Get and validate user's 5-letter guess from words.is_valid_guess()
    #   - Get color list via evaluate_guess(guess, secret_word, difficulty)
    #   - Append (guess, feedback) to `board_history`
    #   - Call board.display_board(board_history, max_tries) to print full board state
    #   - If the user guess the right secret word: Calculate time, call results and return
    # Step 5: If out of tries:
    #   - Calculate time, call results, and return
    pass