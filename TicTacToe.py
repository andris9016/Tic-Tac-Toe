import os
import time
import random


# Print the header
def print_header():
    print("""
             Welcome our first Tic-Tac-Toe Game           1 | 2 | 3
        The palces where you should put your character:   4 | 5 | 6
                                                          7 | 8 | 9
       """)


def menu():
    print("""
            Menu
            ---------------------------
            1. Single player
            2. Multiplayer
            3. Exit """)

    # Handle the user input
    correct_input = False
    while not correct_input:
        try:
            selection = int(input("Enter your option (1-3): ".strip()))
            if selection < 1 or selection > 3:
                print("The number should be between 1 and 9")
                continue
        except ValueError:
            print("Please enter a number between 1-9")
        else:
            correct_input = True

    return selection


def print_board(board):
    print("""
                      %s |  %s  | %s
                     -------------
                      %s |  %s  | %s
                     -------------
                      %s |  %s  | %s
        """ % (board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))


# Put the character, where the player want
def handle_input():
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
    return move


# Check if a space is already taken, put the icon in the table
def player_move(board, icon):
    move = handle_input()
    if board[move - 1] == " ":
        board[move - 1] = icon
    else:
        print("This space is not empty. Try it again!")
        time.sleep(1)


# Check if one of the player wins
def is_winner(board, icon):
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


def computer_move(board, icon):
    if board[4] == " ":
        board[4] = icon
        return None

    move = random.randint(1, 9)
    while board[move - 1] != " ":
        move = random.randint(1, 9)
    board[move - 1] = icon


# Check for a tie
def is_tie(board):
    if " " not in board:
        return True
    else:
        return False


def main():
    board = [" " for i in range(9)]
    while True:
        os.system("clear")
        print_header()
        # print_board(board)
        menu()

        print("X turns")
        player_move(board, "X")
        os.system("clear")
        print_header()
        print_board(board)

        if is_winner(board, "X"):
            print("Congratulations! X wins!")
            break
        if is_tie(board):
            print("It's a Tie!")
            break

        print("O turns")
        # player_move(board, "O")
        computer_move(board, "O")
        os.system("clear")
        print_header()
        print_board(board)

        if is_winner(board, "O"):
            print("Congratulations! O wins!")
            break
        if is_tie(board):
            print("It's a Tie!")
            break


main()
