import random

# Define the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Define the winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")

# Function to check if the board is full
def is_board_full(board):
    return " " not in board

# Function to check if a player has won
def check_win(board, player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to make a move on the board
def make_move(board, position, player):
    board[position] = player

# Function for the AI player using Minimax with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player):
    if check_win(board, "X"):
        return -1
    elif check_win(board, "O"):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for the AI player
def find_best_move(board):
    best_move = None
    best_eval = float("-inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            eval = minimax(board, 0, False)
            board[i] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
while True:
    print_board(board)

    # Player's move
    player_move = int(input("Enter your move (1-9): ")) - 1
    if board[player_move] != " " or player_move < 0 or player_move > 8:
        print("Invalid move. Try again.")
        continue

    make_move(board, player_move, "X")

    # Check if the player wins
    if check_win(board, "X"):
        print_board(board)
        print("You win!")
        break

    # Check if the game is a draw
    if is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break

    # AI's move
    ai_move = find_best_move(board)
    make_move(board, ai_move, "O")

    # Check if the AI wins
    if check_win(board, "O"):
        print_board(board)
        print("AI wins!")
        break
