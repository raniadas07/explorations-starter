"""
board.py
Module user experience: print welcome, rules regards to each mode, print the board layout turn-by-turn,
a completion timer, and a leaderboard.
"""

# Declare the display color codes for the text box: GREEN_TILE, YELLOW_TILE, GRAY_TILE

def print_welcome():
    """Display the welcome banner when the game starts."""
    # Print the game title header
    pass


def print_game_rules(difficulty, max_tries):
    """Display the rules, number of tries, and color legend for the chosen mode."""
    # Step 1: Print the selected mode name and max_tries
    # Step 2: If 'easy' or 'medium', explain Green, Yellow, and Gray tiles
    # Step 3: If 'hard', explain only Yellow and Gray tiles
    pass

def display_board(board_history, max_tries):
    """ Render the full Wordle board showing all previous guesses
    in color plus empty placeholder rows for remaining attempts."""
    # Step 1: Loop through each (guess, feedback) in `board_history` and print colored tiles
    # Step 2: Calculate remaining_rows = max_tries - len(board_history)
    # Step 3: Print empty rows for remaining_rows
    pass

def display_wordle_tiles(guess, feedback):
    """Print the guessed word with Green, Yellow, or Gray colored tiles."""
    # Step 1: Pair each letter in guess with its color status in feedback
    # Step 2: Format each letter with the matching background color (Green/Yellow/Gray)
    # Step 3: Print the row of 5 colored tiles to the console
    pass


def display_game_results(won, secret_word, attempts_used):
    """Display win/loss message, secret word, and total time taken."""
    # Step 1: Print victory or game-over message with secret_word
    # Step 2: Format and print `elapsed_time` 
    pass

def display_stats(stats):
    """ Display the player's saved statistics loaded from stats.txt."""
    # Step 1: Print total games played, total wins, and win percentage
    # Step 2: Print the fastest win time (best_time) if the player has at least 1 win
    pass