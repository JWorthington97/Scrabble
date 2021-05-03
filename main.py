from pregame import create_scrabble_board, create_letter_bag, create_letter_values, create_hashed_dictionary, create_player_hands, assign_starting_hand
from midgame import show_scrabble_board


# Initialises empty board
board = create_scrabble_board()

show_scrabble_board(board)

bag = create_letter_bag()

letter_values = create_letter_values()

#Not hashed yet
the_dictionary = create_hashed_dictionary('small_dictionary_test.txt')
print(bag)
#Define users hand
player_hands = create_player_hands(2, 0, bag)
print(player_hands)

print(bag)

show_scrabble_board(board)
