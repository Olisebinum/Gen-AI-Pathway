"""
Rock, Paper, Scissors
Module 1 - Beginner Deliverable
Generative AI & Data Science Pathway
"""

import random

# ── 1. Define the possible choices ──────────────────────────────────────────
CHOICES = ["rock", "paper", "scissors"]

# Rules: key beats value
WINS_AGAINST = {
    "rock":     "scissors",
    "paper":    "rock",
    "scissors": "paper",
}

# ── 2. Helper functions ──────────────────────────────────────────────────────

def get_user_choice():
    """Prompt the user until they enter a valid choice."""
    print("\nChoices: rock | paper | scissors")
    while True:
        choice = input("Your choice: ").strip().lower()
        if choice in CHOICES:
            return choice
        print(f"  ✗ '{choice}' is not valid. Please enter rock, paper, or scissors.")


def get_computer_choice():
    """Generate a random choice for the computer."""
    choice = random.choice(CHOICES)
    print(f"Computer chose: {choice}")
    return choice


def determine_winner(user, computer):
    """
    Return the result from the user's perspective:
      'win', 'lose', or 'draw'
    """
    if user == computer:
        return "draw"
    elif WINS_AGAINST[user] == computer:
        return "win"
    else:
        return "lose"


def display_result(result):
    """Print a human-friendly result message."""
    messages = {
        "win":  "🎉 You win!",
        "lose": "💀 You lose!",
        "draw": "🤝 It's a draw!",
    }
    print(messages[result])


# ── 3. Main game loop ────────────────────────────────────────────────────────

def play_game():
    """Run one full round of Rock, Paper, Scissors."""
    print("\n" + "=" * 40)
    print("       ROCK  ✊  PAPER  ✋  SCISSORS  ✌️")
    print("=" * 40)

    user_choice     = get_user_choice()          # Step 2: get user's choice
    computer_choice = get_computer_choice()      # Step 3: generate computer's choice
    result          = determine_winner(user_choice, computer_choice)  # Step 4: determine winner

    print(f"\n  You: {user_choice}  vs  Computer: {computer_choice}")
    display_result(result)

    return result


def main():
    """Entry point — keeps score across multiple rounds."""
    score = {"win": 0, "lose": 0, "draw": 0}

    print("\nWelcome to Rock, Paper, Scissors!")

    while True:
        result = play_game()
        score[result] += 1

        print(f"\nScore → You: {score['win']}  |  Computer: {score['lose']}  |  Draws: {score['draw']}")

        again = input("\nPlay again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing! Final score:")
            print(f"  Wins: {score['win']}  Losses: {score['lose']}  Draws: {score['draw']}")
            break


if __name__ == "__main__":
    main()
