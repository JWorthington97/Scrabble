from board_functions import *
from bag_functions import *
from player_functions import *
from word_functions import *


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

show_scrabble_board(board)


# * = 2* letter
# ^ = 3* letter
# £ = 2* word



