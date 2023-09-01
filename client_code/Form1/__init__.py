# Tic-Tac-Toe game in python

# Define the board as a list of 9 elements
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

# Define the symbols for the players
X = "X"
O = "O"

# Define a function to display the board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

# Define a function to check if the board is full
def is_full():
    return " " not in board

# Define a function to check if a player has won
def has_won(symbol):
    # Check horizontal lines
    if board[0] == board[1] == board[2] == symbol:
        return True
    if board[3] == board[4] == board[5] == symbol:
        return True
    if board[6] == board[7] == board[8] == symbol:
        return True
    # Check vertical lines
    if board[0] == board[3] == board[6] == symbol:
        return True
    if board[1] == board[4] == board[7] == symbol:
        return True
    if board[2] == board[5] == board[8] == symbol:
        return True
    # Check diagonal lines
    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[2] == board[4] == board[6] == symbol:
        return True
    # No winner
    return False

# Define a function to get the valid moves from the board
def get_valid_moves():
    moves = []
    for i in range(len(board)):
        if board[i] == " ":
            moves.append(i)
    return moves

# Define a function to get the user's move
def get_user_move(symbol):
    valid_moves = get_valid_moves()
    while True:
        try:
            move = int(input(f"Enter your move for {symbol} (0-8): "))
            if move in valid_moves:
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

# Define a function to get the computer's move using a random choice
import random

def get_computer_move(symbol):
    valid_moves = get_valid_moves()
    move = random.choice(valid_moves)
    print(f"Computer's move for {symbol} is {move}")
    return move

# Define a function to play the game
def play_game():
    # Display the initial board
    display_board()

    # Loop until the game is over
    while True:
        # Get the user's move for X and update the board
        user_move = get_user_move(X)
        board[user_move] = X

        # Display the updated board
        display_board()

        # Check if the user has won or the board is full
        if has_won(X):
            print("You win!")
            break
        if is_full():
            print("It's a tie!")
            break

        # Get the computer's move for O and update the board
        computer_move = get_computer_move(O)
        board[computer_move] = O

        # Display the updated board
        display_board()

        # Check if the computer has won or the board is full
        if has_won(O):
            print("You lose!")
            break
        if is_full():
            print("It's a tie!")
            break

# Start the game
play_game()
