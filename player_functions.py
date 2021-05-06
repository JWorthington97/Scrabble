from random import randint, choice
from bag_functions import remove_letter_from_bag

def create_player_hands(number_of_players, number_of_ai, bag):
    #if number_of_players + number_of_ai > 4
    #print "Please only provide 4 players"
    player_hands = []
    for player in range(number_of_players):
        print(player)
        player_hands.append(assign_starting_hand(bag))
        player_hands[player].append(None) # make sure to remove
    return player_hands

def assign_starting_hand(bag):
    starting_hand = []
    for i in range(0,7):
        letter = chr(randint(65,90))
        # When assigning letters in the midgame function, we will need to check whether remove_letter_from_bag returns True/False
        remove_letter_from_bag(letter, bag)
        starting_hand.append(letter)
    return starting_hand

def add_letter_to_hand(player_hands, player_index, bag):
    letter = choice(list(bag))
    if remove_letter_from_bag(letter, bag):
        if None not in player_hands[player_index]:
            return False
        else:    
            none_index = player_hands[player_index].index(None)
            player_hands[player_index][none_index] = letter
            return True
