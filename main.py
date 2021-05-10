from board_functions import *
from bag_functions import *
from player_functions import *
from word_functions import *
import pprint

# Initialises empty board
board = create_scrabble_board()

show_scrabble_board(board)

bag = create_letter_bag()

letter_values = create_letter_values()

#Not hashed yet
the_dictionary = create_hashed_dictionary('small_dictionary_test.txt')
#Define users hand
player_hands = create_player_hands(2, 0, bag)
print(player_hands[0])

print(bag)

#show_scrabble_board(board)

#This function will be used after somebody's turn

add_letter_to_hand(player_hands, 0, bag) # we need to pass in correct player index
print(player_hands[0])
print(bag)

board[6][7] = 'L'
board[7][7] = 'E'
board[8][7] = 'M'
board[9][7] = 'O'
board[10][7] ='N'

board[3][5] = '*'

board[6][8] = 'O'
board[6][9] = 'V'
board[6][10] = 'E'

board[8][5] = 'S'
board[8][6] = 'A'

board[3][6] = 'T'

board[7][8] = 'T'
board[8][8] = 'H'
board[9][8] = 'E'
board[10][8] = 'R'

show_scrabble_board(board)

# receive word, location, direction
# find all the collisions on the board, and save them all as words
# check all of the words
#if ONE is not a word, can't put the received word down
# 6              L O V E
# 7              E T
# 8          S A M H
# 9              O E
#10              N R

#function to get array of collision words
#function to check them all (already got)
#function to add to board
#function to check proposed word, direction, location not impeding another word


# * = 2* letter
# ^ = 3* letter
# £ = 2* word

# proposed_word = input("Provide word: ")
# proposed_location = input("Location: ")
# proposed_direction = input("Direction (Up, Right, Down): ")
proposed_word = 'tortoise'
proposed_location = 'H1'
proposed_direction = 'Right'
word_check = add_word_to_board(proposed_word, proposed_location, proposed_direction,board)
if word_check == -1:
    print("Word is invalid. Please ensure you only use characters.")
# need to add while loop/try/catch etc for when when the function returns -1, -2, -3, or -4
#while add_word_to_board(proposed_word, proposed_location, proposed_direction,board) != 0:
    
show_scrabble_board(board)


