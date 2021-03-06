import os
import time
import random


def print_header():
    print("""
               Welcome to our Tic-Tac-Toe Game            1 | 2 | 3  
        The palces where you should put your character:   4 | 5 | 6
                                                          7 | 8 | 9
       """)

# Prints the picture when the user exits the menu
def print_symbol():
    read_file = open("symbol.txt", "r")
    content = read_file.read()
    print(content)


def menu():
    print("""
            Menu
            ---------------------------
            1. Single player
            2. Multiplayer
            3. Exit
            ---------------------------
            """)

    # Handle the user input
    correct_input = False
    while not correct_input:
        try:
            selection = int(input(" "*12 + "Enter your option (1-3): ".strip()))
            if selection < 1 or selection > 3:
                print("The number should be between 1 and 3")
                continue
        except ValueError:
            print("Please enter a number between 1 and 3")
        else:
            correct_input = True

    return selection


def print_board(board):
    print("""
                    ╔═══╦═══╦═══╗
                    ║ %s ║ %s ║ %s ║
                    ╠═══╬═══╬═══╣
                    ║ %s ║ %s ║ %s ║
                    ╠═══╬═══╬═══╣
                    ║ %s ║ %s ║ %s ║
                    ╚═══╩═══╩═══╝
        """ % (board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))



# Places the move, if it's correct
def player_move(board, icon):    
    empty = False
    while not empty:
        try:
            move = int(input("Enter your move (1-9): ".strip()))
            if move < 1 or move > 9:
                print("The number should be between 1 and 9")
            elif board[move - 1] != " ":
                print("This space is not empty. Try it again!")
                time.sleep(2)
                update_table(board)
            else:
                board[move - 1] = icon
                empty = True
        except ValueError:
            print("Please enter a number between 1 and 9")


# The AI checks if a space is already taken, puts the icon on the table
def computer_move(board, icon):
    if board[4] == " ":
        board[4] = icon
        return None

    move = random.randint(1, 9)
    while board[move - 1] != " ":
        move = random.randint(1, 9)
    board[move - 1] = icon


# Checks if one of the player won the game
def is_winner(board, icon, name):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[2] == icon and board[4] == icon and board[6] == icon):
        print("Congratulations!", name, "won the game!")
        return True
    else:
        return False


# Checks if there's place left to mark
def is_board_full(board):
    if " " not in board:
        print("Game is over")
        return True
    else:
        return False


def update_table(board):
    os.system("clear")
    print_header()
    print_board(board)


def single_player(board, option):
    player1_name = input(" "*12 + "Enter your name: ")
    while option == 1:
        update_table(board)
        print(player1_name, "\'s turn")
        player_move(board, "X")
        update_table(board)
        if check_win_tie(board, "X", player1_name):
            break
        computer_move(board, "O")
        update_table(board)
        if check_win_tie(board, "O", "The computer"):
            break

def multiplayer(board, option):
    player1_name = input(" "*12 + "First player's name: ")
    player2_name = input(" "*12 + "Second player's name: ")
    while option == 2:
        update_table(board)
        print(player1_name + "\'s turn")
        player_move(board, "X")
        update_table(board)
        if check_win_tie(board, "X", player1_name):
            play_again(board, option)
        print(player2_name + "\'s turn")
        player_move(board, "O")
        update_table(board)
        if check_win_tie(board, "O", player2_name):
            play_again(board, option)

def play_again(board, option):
    choice = input("Do you want to play again?")
    if choice == "Y" or "y":
        board = [" " for i in range(9)]
        update_table(board)        
        version = input("Single or Multi?")
        if version == "Single":
            option = 1
            return option, board


# Checks if the game is over
def check_win_tie(board, icon, player):
    return is_winner(board, icon, player)
    return is_board_full(board)
        

def main():
    board = [" " for i in range(9)]
    print_header()
    option = menu()
    # Single player option
    if option == 1:
        single_player(board, option)
    # Multiplayer option
    elif option == 2:
        multiplayer(board, option)
    # Exit option
    elif option == 3:
        os.system("clear")
        print_symbol()


main()
