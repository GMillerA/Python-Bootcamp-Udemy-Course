# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:13:35 2017

@author: Galen Miller

Milestone Project 1 for Python Course
"""
# For using the same code in either Python 2 or 3
#from __future__ import print_function 
from __future__ import print_function
from IPython.display import clear_output
## Note: Python 2 users, use raw_input() to get player input. Python 3 users, use input()
##Step 1: Write a function that can print out a board.
##Set up board as 3x3 representation of a list
clear_output

def display_board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
#Think about using while loops to continually ask until you get a correct answer.
def player_input():
    global player1_name
    global player2_name
    player1_name = raw_input("Enter Player 1 Name: ")
    player2_name = raw_input("Enter Player 2 Name: ")
    return player1_name
    return player2_name

    
    

#Step 3: Step 3: Write a function that takes, in the board list object, 
#a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board 
def place_marker(board, marker, position):
    position = int(position)
    board[position] = marker
    
#Step 4: Write a function that takes in a board and a mark (X or O) 
#and then checks to see if that mark has won.       
def win_check(board,marker):
    global game_on
    if marker==board[0]==board[1]==board[2] or marker==board[3]==board[4]==board[5] or marker==board[6]==board[7]==board[8] or marker==board[0]==board[3]==board[6] or marker==board[1]==board[4]==board[7] or marker==board[2]==board[5]==board[8] or marker==board[0]==board[4]==board[8] or marker==board[2]==board[4]==board[6]:
        #print("The winner is: %s!") %(current_player) 
        print("Winner!")
        game_on = False 
        replay()
        
#Step 5: Write a function that uses the random module to randomly decide which player goes first. 
#You may want to lookup random.randint() Return a string of which player went first.
import random #import randint
def choose_first():
    start = random.randint(0,1)
    global player1_name
    global player2_name
    global current_player
    if start == 0: 
        print("Player 1: X goes first!") 
        current_player = player1_name
    else: 
        print("Player 2: O goes first!") #%(player2_name)
        current_player = player2_name
#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    if board[position]=="":
        return True
    else:
        return False
        print("Space is not available")
#Step 7: Write a function that checks if the board is full and returns a boolean value. 
#True if full, False otherwise.
def full_board_check(board):
    count_used = 0
    for x in board:
        if board[x]=="":
            return False
        else: 
            count_used += 1
    if count_used == 9:
        return True
#Step 8: Write a function that asks for a player's next position (as a number 1-9)
#and then uses the function from step 6 to check if its a free position. 
#If it is, then return the position for later use.
def player_choice(position):
    global board
    if space_check(board, position) == True:
        return position
    else: 
        print("Space is not available") 
#Step 9: Write a function that asks the player if they want to play again and 
#returns a boolean True if they do want to play again.
def replay():
    global game_on
    s = raw_input("Want to play again?")
    if s == "yes":
        return True
    else: 
        game_on = False
#Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
def tic_tac_toe():
    # Set the game up here
    clear_output()
    board = [0,0,0,0,0,0,0,0,0]
    game_on = True
    player1_name = " "
    player2_name = " "
    current_player = " "
    player_input()
    choose_first()
    
    while game_on == True:
        #Player 1 Turn
        while current_player == player1_name:
            marker = "X"
            p = raw_input("Position? : ")
            #if full_board_check == False:
                #player_choice(board, p)
            place_marker(board, marker, p)
            display_board(board)
            win_check(board, marker)
            #if not replay():
                #game_on = False
                #break
            print("Now Player 2's Move")
            current_player = player2_name
            break
            
        
        
        # Player2's turn.
        while current_player == player2_name:
            marker = "O"
            p = raw_input("Position? : ")
            if full_board_check == True:
                #player_choice(board, p)
                place_marker(board, marker, p)
            display_board(board)
            win_check(board, marker)
            #if not replay():
                #game_on = False
                #break
            print("Now Player 1's Move")
            current_player = player1_name
            break
    

        
        