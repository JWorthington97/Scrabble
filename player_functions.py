from random import randint, choice, choices
from bag_functions import remove_letter_from_bag

def create_player_hands(number_of_players, number_of_ai, bag):
    #if number_of_players + number_of_ai > 4
    #print "Please only provide 4 players"
    player_hands = []
    for player in range(number_of_players):
        print(player)
        player_hands.append(assign_starting_hand(bag))
    return player_hands

def assign_starting_hand(bag):
    starting_hand = []
    for i in range(0,7):
        #letter = chr(randint(65,90))
        letter = choices(list(bag.keys()), weights=bag.values(), k=1)[0]
        # When assigning letters in the midgame function, we will need to check whether remove_letter_from_bag returns True/False
        remove_letter_from_bag(letter, bag)
        starting_hand.append(letter)
    return starting_hand

def add_letter_to_hand(player_hands, player_index, bag):
    letter = choices(list(bag.keys()), weights=bag.values(), k=1)[0]
    if remove_letter_from_bag(letter, bag):
        if None not in player_hands[player_index]:
            return False
        else:    
            none_index = player_hands[player_index].index(None)
            player_hands[player_index][none_index] = letter
            return True

def remove_letters_from_hand(player_hand, proposed_word, proposed_location, proposed_direction, board):
    letters_to_remove = []
    new_hand = []
    word = proposed_word.strip().upper()
    direction = proposed_direction.strip().upper()
    column = ord(proposed_location[0].upper().strip()) - 65 # ASCII value for 'A'
    row = int(proposed_location[1::])

    for index, letter in enumerate(word):
        if direction in ['R', 'RIGHT']:
            if board[row][column + index] == ' ':
                letters_to_remove.append(letter)
        else: # For Down
            if board[row + index][column] == ' ':
                letters_to_remove.append(letter)
    for letter in letters_to_remove:
        player_hand[player_hand.index(letter)] = None
    return player_hand