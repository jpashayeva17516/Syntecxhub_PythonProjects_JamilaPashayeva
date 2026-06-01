
import random

# ──────────────────────────────────────────
#  DIFFICULTY SETTINGS
# ──────────────────────────────────────────
def get_difficulty():
    """Ask the player to choose a difficulty and return the number range."""
    print("\n┌─────────────────────────────┐")
    print("│      Select Difficulty       │")
    print("├─────────────────────────────┤")
    print("│  1. Easy    →  1  to  50    │")
    print("│  2. Medium  →  1  to  100   │")
    print("│  3. Hard    →  1  to  200   │")
    print("└─────────────────────────────┘")

    while True:
        choice = input("Enter choice (1 / 2 / 3): ").strip()
        if choice == "1":
            return 1, 50, "Easy"
        elif choice == "2":
            return 1, 100, "Medium"
        elif choice == "3":
            return 1, 200, "Hard"
        else:
            print("  ⚠  Invalid choice. Please enter 1, 2, or 3.")


# ──────────────────────────────────────────
#  CORE GAME LOGIC
# ──────────────────────────────────────────
def play_game(low, high, level):
    """Run one round of the game. Returns the number of attempts taken."""
    secret = random.randint(low, high)
    attempts = 0

    print(f"\n  🎯  [{level} Mode]  Guess a number between {low} and {high}.")
    print("       Type 'quit' at any time to exit.\n")

    while True:
        raw = input("  Your guess: ").strip().lower()

        # Allow the player to quit mid-game
        if raw == "quit":
            print(f"\n  The number was {secret}. Better luck next time!")
            return None

        # Validate input
        try:
            guess = int(raw)
        except ValueError:
            print("  ⚠  Please enter a whole number.")
            continue

        if guess < low or guess > high:
            print(f"  ⚠  Number must be between {low} and {high}.")
            continue

        attempts += 1

        # Give a hint
        if guess < secret:
            print("  📉  Too LOW!  Try a higher number.")
        elif guess > secret:
            print("  📈  Too HIGH! Try a lower number.")
        else:
            print(f"\n  ✅  Correct! The number was {secret}.")
            print(f"  🔢  You guessed it in {attempts} attempt(s).")
            return attempts


# ──────────────────────────────────────────
#  SCORE TRACKER
# ──────────────────────────────────────────
def show_scoreboard(scores):
    """Display all round scores and the current best."""
    if not scores:
        return
    print("\n  📊  Scoreboard:")
    for i, s in enumerate(scores, 1):
        print(f"       Round {i}: {s} attempt(s)")
    print(f"  🏆  Best Score: {min(scores)} attempt(s)")


# ──────────────────────────────────────────
#  MAIN LOOP
# ──────────────────────────────────────────
def main():
    print("\n" + "=" * 42)
    print("    🎮  Number Guessing Game  🎮")
    print("=" * 42)

    scores = []   # Store attempts for each completed round

    while True:
        # Choose difficulty
        low, high, level = get_difficulty()

        # Play one round
        result = play_game(low, high, level)

        if result is not None:
            scores.append(result)

            # Check for a new best score
            if len(scores) == 1 or result == min(scores):
                print("  🌟  New best score!")

            # Show the scoreboard
            show_scoreboard(scores)

        # Ask to play again
        print()
        again = input("  Play again? (yes / no): ").strip().lower()
        if again in ("yes", "y"):
            continue
        else:
            print("\n  Thanks for playing! Goodbye 👋")
            print("=" * 42 + "\n")
            break


# ──────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────
if __name__ == "__main__":
    main()