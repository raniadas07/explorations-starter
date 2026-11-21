"""
main.py
Manages the difficulty selection menu, coordinates other modules, and maintains the game loop (including the "Play again?" Yes/No prompt).
"""

# import fucntions from words.py, game.py, và board.py

def load_stats():
    """Load saved player statistics, or initialize defaults if file is not created yet."""
    # Step 1: Try opening `filename` and parsing data into a dictionary
    # Step 2: If file does not exist yet, return default dict:
    #         {"games_played": 0, "wins": 0, "best_time": None}
    pass

def reset_stats(filename="stats.txt"):
    """Reset all saved statistics in stats.txt back to zero."""
    # Step 1: Create a clean default dictionary {"games_played": 0, "wins": 0, "losses": 0, "best_time": None}
    # Step 2: Overwrite `filename` with the reset dictionary and return it
    pass

def update_stats(stats, won, elapsed_time, filename="stats.txt"):
    """Update stats after a round and save them back to stats.txt."""
    # Step 1: Append stats"games_played" by 1
    # Step 2: If `won` is True:
    #   - Append stats["wins"] by 1
    #   - If stats["best_time"] is None or elapsed_time < stats["best_time"]:
    #       update stats["best_time"] = elapsed_time
    # Step 3: Else (`won` is False): Append stats["losses"] by 1
    # Step 4: Save updated `stats` dictionary back to `filename`
    pass

def choose_difficulty():
    """Prompt the user to select Easy, Medium, or Hard mode."""
    # Step 1: Display the question
    # Step 2: Loop until the user enters a valid mode choice
    # Step 3: Return the validated difficulty string
    pass


def play_again_prompt():
    """Ask the user if they want to play another round ('Yes' or 'No')."""
    # Step 1: Ask the user "Would you like to continue playing? (Yes/No)"
    # Step 2: Validate input so only 'Yes' or 'No' is accepted
    # Step 3: Return True if 'Yes', False if 'No'
    pass


def main():
    """Main entry point that controls the program."""
    # Step 1: Call board.print_welcome() to show the game title
    # Step 2: Call `stats = load_stats()` to retrieve past data from stats.txt
    # Step 3: Start the outer game loop (runs while keep_playing is True)
    #   - Prompt the user to select their preferred difficulty mode.
    #   - Load the matching word list for that difficulty and randomly pick a secret word from the words module.
    #   - Run a full round of the game in the game module, tracking whether the player won and how long it took.
    #   - Update the player's win, loss, and best time records and save the new data to stats.txt.
    #   - Display the updated lifetime statistics through the board module.
    #   - Ask the player if they want to play again to determine whether to repeat the loop.
    # Step 4: If they player doesn't want to continue playing, ask to reset stats:
    #   - Ask if the user want to reset stats
    #   - If no, keep the stats. If yes, delete past stats and renew stats
    # Step 5: Print goodbye message and terminate program
    pass