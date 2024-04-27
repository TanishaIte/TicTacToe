import os
import time

# Constants for game state
Running = 0
Win = 1
Draw = -1

def initialize_game():
    global board, player, Game, Mark
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = 1
    Game = Running
    Mark = 'X'

def draw_board():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))

def check_position(x):
    if board[x] == ' ':
        return True
    else:
        return False

def check_win():
    global Game
    if board[1] == board[2] == board[3] != ' ' or \
       board[4] == board[5] == board[6] != ' ' or \
       board[7] == board[8] == board[9] != ' ' or \
       board[1] == board[4] == board[7] != ' ' or \
       board[2] == board[5] == board[8] != ' ' or \
       board[3] == board[6] == board[9] != ' ' or \
       board[1] == board[5] == board[9] != ' ' or \
       board[3] == board[5] == board[7] != ' ':
        Game = Win
    elif all(cell != ' ' for cell in board[1:]):
        Game = Draw
    else:
        Game = Running

def play_game():
    print(" Welcome to Tic Tac Toe Game. All The Best !! 👍" )
    print("Player 1 [O] --- Player 2 [X]\n")
    print()
    print()
    print("Please Wait...")
    time.sleep(2)
    
    global player
    while Game == Running:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board()
        if player % 2 != 0:
            print("Player 1's Turn !")
            Mark = 'X'
        else:
            print("Player 2's Turn !")
            Mark = 'O'
        choice = int(input("Enter the position between [1-9] where you want to mark. Choose wisely: "))
        if 1 <= choice <= 9:
            if check_position(choice):
                board[choice] = Mark
                player += 1
                check_win()
                if Game != Running:  # Check if the game has ended
                    break  # If the game has ended, exit the loop
            else:
                print("That position is already marked. Choose another.")
        else:
            print("Invalid input. Choose a position between 1 and 9.")

    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board()
    if Game == Draw:
        print("Game Draw 👍")
    elif Game == Win:
        if player % 2 != 0:
            print("Player 1 Won 😊")
        else:
            print("Player 2 Won 😊")
    
    # Prompt players to play again
    if play_again():
        initialize_game()
        play_game()
    else:
        print("Thanks for playing!")

def play_again():
    return input("Do you want to play again? (y/n): ").lower().strip() == 'y'

# Start the game
initialize_game()
play_game()
