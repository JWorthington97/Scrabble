from random import randint

# function initialises an empty board array
def create_scrabble_board():
    # double spaces here because of the 2*
    return [['  '] * 15]* 15

def create_player_hands(number_of_players, number_of_ai, bag):
    #if number_of_players + number_of_ai > 4
    #print "Please only provide 4 players"
    player_hands = []
    for player in range(number_of_players):
        print(player)
        player_hands.append(assign_starting_hand(bag))
    return player_hands

def create_letter_bag():
    pregame_bag = {
        'A': 9,
        'B': 2,
        'C': 2,
        'D': 4,
        'E': 12,
        'F': 2,
        'G': 3,
        'H': 2,
        'I': 9,
        'J': 1,
        'K': 1,
        'L': 4,
        'M': 2,
        'N': 6,
        'O': 8,
        'P': 2,
        'Q': 1,
        'R': 6,
        'S': 4,
        'T': 6,
        'U': 4,
        'V': 2,
        'W': 2,
        'X': 1,
        'Y': 2,
        'Z': 1
        # Blank:2 tile if we get to it
    }
    return pregame_bag

def create_letter_values():
    letter_values = {
        #'BLANK': 0,
        'A':1,
        'B':3,
        'C':3,
        'D':2,
        'E':1,
        'F':4,
        'G':2,
        'H':4,
        'I':1,
        'J':8,
        'K':5,
        'L':1,
        'M':3,
        'N':1,
        'O':1,
        'P':3,
        'Q':10,
        'R':1,
        'S':1,
        'T':1,
        'U':1,
        'V':4,
        'W':4,
        'X':8,
        'Y':4,
        'Z':10
    }
    return letter_values    

def create_hashed_dictionary(dictionary_path):
    dictionary = {}
    with open(dictionary_path, 'r') as dictionary_file:
        for word in dictionary_file:
            # add hashing algorithm in here
            dictionary[word.strip()] = None
    return dictionary

def assign_starting_hand(bag):
    starting_hand = []
    for i in range(0,7):
        letter = chr(randint(65,90))
        # When assigning letters in the midgame function, we will need to check whether remove_letter_from_bag returns True/False
        remove_letter_from_bag(letter, bag)
        starting_hand.append(letter)
    starting_hand.append(None)
    return starting_hand

def remove_letter_from_bag(letter, bag):
    if bag[letter] == 0:
        return False
    else:
        bag[letter] -= 1
        return True

