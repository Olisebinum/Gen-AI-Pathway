"""
Tic-Tac-Toe AI Agent (Minimax)
Module 1 – Beginner Deliverable
Generative AI & Data Science Pathway
"""

import math

# ── 1. Define the game board ─────────────────────────────────────────────────
def create_board():
    """Return a fresh 3x3 board represented as a list of 9 cells."""
    return [" " for _ in range(9)]


def display_board(board):
    """Print the board in a readable grid format."""
    print("\n")
    for row in range(3):
        cells = board[row * 3: row * 3 + 3]
        print("  " + " | ".join(cells))
        if row < 2:
            print("  " + "-" * 9)
    print()


def display_positions():
    """Show the position numbers so the user knows where to play."""
    print("  Board positions:")
    for row in range(3):
        nums = [str(row * 3 + col + 1) for col in range(3)]
        print("  " + " | ".join(nums))
        if row < 2:
            print("  " + "-" * 9)
    print()


# ── 2. Check if a player has won ─────────────────────────────────────────────
WIN_COMBINATIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
    [0, 4, 8], [2, 4, 6],              # diagonals
]

def check_winner(board, player):
    """Return True if the given player has a winning combination."""
    return any(
        all(board[cell] == player for cell in combo)
        for combo in WIN_COMBINATIONS
    )


# ── 3. Check if the game is a tie ────────────────────────────────────────────
def check_tie(board):
    """Return True if all cells are filled and no one has won."""
    return " " not in board


def get_available_moves(board):
    """Return list of indices that are still empty."""
    return [i for i, cell in enumerate(board) if cell == " "]


# ── AI: Minimax algorithm ────────────────────────────────────────────────────
def minimax(board, is_maximizing):
    """
    Recursively evaluate board states.
    AI  = 'O' (maximizer, wants highest score)
    User = 'X' (minimizer, wants lowest score)
    """
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if check_tie(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for move in get_available_moves(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "
            best = max(best, score)
        return best
    else:
        best = math.inf
        for move in get_available_moves(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = " "
            best = min(best, score)
        return best


def get_ai_move(board):
    """Return the best move index for the AI using Minimax."""
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


# ── 4. Main game loop ────────────────────────────────────────────────────────
def main():
    print("\n" + "=" * 40)
    print("       TIC-TAC-TOE  |  You vs AI")
    print("=" * 40)
    print("  You = X    |    AI = O")
    display_positions()

    board = create_board()
    current_player = "X"          # User always goes first

    while True:
        display_board(board)

        if current_player == "X":
            # --- User turn ---
            while True:
                try:
                    pos = int(input("  Enter position (1-9): ")) - 1
                    if pos < 0 or pos > 8:
                        print("  ✗ Enter a number between 1 and 9.")
                    elif board[pos] != " ":
                        print("  ✗ That position is already taken.")
                    else:
                        break
                except ValueError:
                    print("  ✗ Please enter a valid number.")
            board[pos] = "X"

        else:
            # --- AI turn ---
            print("  AI is thinking...")
            move = get_ai_move(board)
            board[move] = "O"
            print(f"  AI played position {move + 1}")

        # Check result after every move
        if check_winner(board, current_player):
            display_board(board)
            if current_player == "X":
                print("  🎉 You win! Well played!\n")
            else:
                print("  🤖 AI wins! Better luck next time.\n")
            break

        if check_tie(board):
            display_board(board)
            print("  🤝 It's a tie!\n")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    # Play again?
    again = input("  Play again? (yes / no): ").strip().lower()
    if again in ("yes", "y"):
        main()
    else:
        print("\n  Thanks for playing!\n")


# ── 5. Call the main game loop ───────────────────────────────────────────────
if __name__ == "__main__":
    main()
