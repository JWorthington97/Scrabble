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

#show_scrabble_board(board)

#This function will be used after somebody's turn

add_letter_to_hand(player_hands, 0, bag) # we need to pass in correct player index

board[6][7] = 'L'
board[7][7] = 'E'
board[8][7] = 'M'
board[9][7] = 'O'
board[10][7] ='N'

board[3][5] = '*'

# board[6][8] = 'O'
# board[6][9] = 'V'
# board[6][10] = 'E'

board[8][5] = 'S'
board[8][6] = 'A'

board[7][10] = 'T'



#function to check them all (already got)
#function to add to board
#function to check proposed word, direction, location not impeding another word


# * = 2* letter
# ^ = 3* letter
# £ = 2* word

# proposed_word = input("Provide word: ")
# proposed_location = input("Location: ")
# proposed_direction = input("Direction (Up, Right, Down): ")
proposed_word = 'OTHER'
proposed_location = 'I6'
proposed_direction = 'Down'
word_check = add_word_to_board(proposed_word, proposed_location, proposed_direction,board)
if word_check == -1:
    print("Word is invalid. Please ensure you only use characters.")
# need to add while loop/try/catch etc for when when the function returns -1, -2, -3, or -4
#while add_word_to_board(proposed_word, proposed_location, proposed_direction,board) != 0:

#We need to check the extra letters in their word that aren't in their hand fit on the board
show_scrabble_board(board)

start_location = [6,8] # = 'I6'
# they provide the whole word e.g OTHER
# if down:
#   if board[row][column] == proposed_word[0] #this means that they want the word to start with O, and so we don't remove it from their hand
#      remove_from_hand
#   if board[row + len(word)][column] == proposed_word[-1]:
#       they want to join on the last letter in the word


# Need to check all words in words_to_test
# Figuring out where they are joining onto the board and then do NOT subtract from the hand
# Write to board (except the characters already on there)

#add_word_to_board('LOVE', 'H6', 'R', board)
show_scrabble_board(board)
#words_to_test = get_words_from_board_right('LOVE', 'H6', board)
#print(words_to_test)
# check all of the words
# if one ISN'T a word - ask user for a different word
# if all ARE words add_word_to_board(words_to_test[0])
#add_word_to_board('LOVE', 'H6', 'R', board)


print(get_words_from_board_right('LOVE', 'H6', board))
get_words_from_board_down