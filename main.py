from board_functions import *
from bag_functions import *
from player_functions import *
from word_functions import *

title_sequence()

# Initialising variables
board = create_scrabble_board()
show_scrabble_board(board)
bag = create_letter_bag()
letter_values = create_letter_values()
dictionary = create_hashed_dictionary('dictionary.txt')
player_hands = create_player_hands(2, 0, bag)
scores = [0, 0] #, 0, 0]
skip = [0, 0] #[0, 0]

# The game:
first_go = 1
end_game = 0
while end_game == 0: # Need to be while all players do NOT pass
    # If both players haven't skipped, continue playing the game
    if skip[0] == 1 and skip[1] == 1:
        end_game = 1
    else:
        skip[0], skip[1] = 0, 0
        for player, hand in enumerate(player_hands):
            if play_round(player, hand, player_hands, scores, dictionary, letter_values, board, bag, first_go) == -1:
                skip[player] = 1  
            first_go = 0 
      
# Deduct remaining tiles to scores
for player, hand in enumerate(player_hands):
    for letter in hand:
        if letter != None:
            scores[player] -= letter_values[letter]
    print(f"Player {player}'s final score is {scores[player]}")

print(f"\nPlayer {scores.index(max(scores))} wins with {max(scores)} points!")


