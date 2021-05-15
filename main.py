from board_functions import *
from bag_functions import *
from player_functions import *
from word_functions import *

# Initialising variables
board = create_scrabble_board()
show_scrabble_board(board)
bag = create_letter_bag()
letter_values = create_letter_values()
dictionary = create_hashed_dictionary('dictionary.txt')
player_hands = create_player_hands(2, 0, bag)
scores = [0, 0, 0, 0]

#This function will be used after somebody's turn
add_letter_to_hand(player_hands, 0, bag) # we need to pass in correct player index

# proposed_word = 'OTHER'
# proposed_location = 'I6'
# proposed_direction = 'Down'
# word_check = add_word_to_board(proposed_word, proposed_location, proposed_direction,board)
# if word_check == -1:
#     print("Word is invalid. Please ensure you only use characters.")

#We need to check the extra letters in their word that aren't in their hand fit on the board
show_scrabble_board(board)

first_go = 1
#for i in range(10):
while True: # Need to be while all players do NOT pass
    for player, hand in enumerate(player_hands):
        print("Player:", player, "Score:", 150)
        print("Hand:", ' '.join(hand))
        proposed_word = None
        proposed_location = None
        proposed_direction = None
        words_to_test = [None] # Set to None so first instance of while loop doesn't error
        
        while are_words_in_dictionary(words_to_test, dictionary) == False:
            if words_to_test != None:
                proposed_word = input("Word: ")
                proposed_location = input("Start location: ")
                proposed_direction = input("Word direction: ")
            while user_input_validity(proposed_word, proposed_location, proposed_direction, board, first_go, player_hands[player]) == False:
                proposed_word = input("Word: ")
                proposed_location = input("Start location: ")
                proposed_direction = input("Word direction: ")
            
            # right or down
            if proposed_direction.strip().upper() in ['R', 'RIGHT']:
                words_to_test = get_words_from_board_right(proposed_word, proposed_location, board)
                print(words_to_test)
            else:
                words_to_test = get_words_from_board_down(proposed_word, proposed_location, board)
                print(words_to_test)

        add_word_to_board(proposed_word, proposed_location, proposed_direction, board)
        player_hands[hand] = remove_letters_from_hand(hand, proposed_word, proposed_location, proposed_direction, board)
        # ^^^ NEED TO FIX THIS BIG
        add_letter_to_hand(player_hands, player, bag)
        show_scrabble_board(board)
        first_go = 0

# Remove from hand logic
# Need to remove all letters from hand other than the ones on the board (in the direction they provided)
# add score