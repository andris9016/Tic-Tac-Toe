import os
import time
# import random

board = [" " for i in range(9)]

# Print the header


def print_header():
    print("""
             Welcome our first Tic-Tac-Toe Game           1 | 2 | 3
        The palces where you should put your character:   4 | 5 | 6
                                                          7 | 8 | 9
       """)

# Print the board


def print_board():
    print("""
                      %s |  %s  | %s
                     -------------
                      %s |  %s  | %s
                     -------------
                      %s |  %s  | %s
        """ % (board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))

# Put the character, where the player want to


def player_move(icon):
    # Handle the user input
    correct_input = False
    while not correct_input:
        try:
            move = int(input("Type your move (1-9): ".strip()))
            if move < 1 or move > 9:
                print("The number should be between 1 and 9")
                continue
        except ValueError:
            print("Please enter a number between 1-9")
        else:
            correct_input = True

    # Check if a space is already taken
    if board[move - 1] == " ":
        board[move - 1] = icon
    else:
        print("This space is not empty. Try it again!")
        time.sleep(1)

# Check if one of the player wins


def is_winner(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

# Check for a tie


def is_tie():
    if " " not in board:
        return True
    else:
        return False


while True:
    os.system("clear")
    print_header()
    print_board()

    print("X turns")
    player_move("X")
    os.system("clear")
    print_header()
    print_board()

    if is_winner("X"):
        print("Congratulations! X wins!")
        break
    if is_tie():
        print("It's a Tie!")
        break

    print("O turns")
    player_move("O")
    os.system("clear")
    print_header()
    print_board()

    if is_winner("O"):
        print("Congratulations! O wins!")
        break
    if is_tie():
        print("It's a Tie!")
        break
