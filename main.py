from board_functions import *
from bag_functions import *
from player_functions import *
from word_functions import *
from time import sleep

# Initialising variables
board = create_scrabble_board()
show_scrabble_board(board)
bag = create_letter_bag()
letter_values = create_letter_values()
dictionary = create_hashed_dictionary('dictionary.txt')
player_hands = create_player_hands(2, 0, bag)
scores = [0, 0, 0, 0]
skip = [0, 0, 0, 0]

# The game:
first_go = 1
end_game = 0
#while count(letters in bag) > 0 or skip[0] != 1 and skip[1] != 1
while end_game == 0: # Need to be while all players do NOT pass
    for player, hand in enumerate(player_hands):
        print(f"\nPlayer {player}'s turn.\nScore: {scores[player]}\nHand: {' '.join(hand)}\n")
        words_to_test = [None] # Set to None so first instance of while loop doesn't error
        
        while are_words_in_dictionary(words_to_test, dictionary) == False:
            if words_to_test != None:
                proposed_word, proposed_location, proposed_direction = input("Word: "), input("Start location: "), input("Word direction: ")
            while user_input_validity(proposed_word, proposed_location, proposed_direction, board, first_go, player_hands[player]) == False:
                proposed_word, proposed_location, proposed_direction = input("Word: "), input("Start location: "), input("Word direction: ")

            # Right or Down
            if proposed_direction.strip().upper() in ['R', 'RIGHT']:
                words_to_test = get_words_from_board_right(proposed_word, proposed_location, board)
                print("Words:", ', '.join(words_to_test))
            else:
                words_to_test = get_words_from_board_down(proposed_word, proposed_location, board)
                print("Words:", ', '.join(words_to_test))

        player_hands[player] = remove_letters_from_hand(hand, proposed_word, proposed_location, proposed_direction, board)
        # replace missing letters in player hand
        for i in range(0,player_hands[player].count(None)):
            add_letter_to_hand(player_hands, player, bag)
        add_word_to_board(proposed_word, proposed_location, proposed_direction, board) 
        round_score = calculate_score(letter_values, words_to_test)
        scores[player] += round_score
        print(f"You scored {round_score} points!\n"), sleep(2), show_scrabble_board(board)
        first_go = 0
        print(bag)
        print(sum(bag.values()))
        print(min(bag.values()))
        #if count of all lettrs in bag == 0, end_game = 1





# Jumble
# Pass logic / End condition

# If no more letters in bag, or both players pass
# You then calculate the scores of the letters in their hand and deduct from final scores and print winner
# The game ends when all letters have been drawn and one player uses his or her last letter; or when all possible plays have been made.
#test what happens when you run out of letters (set dict to all 0)