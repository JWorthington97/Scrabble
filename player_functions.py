from random import randint, choice, choices
from time import sleep
from bag_functions import remove_letter_from_bag
from board_functions import *
from word_functions import *

def create_player_hands(number_of_players, number_of_ai, bag):
    #if number_of_players + number_of_ai > 4
    #print "Please only provide 4 players"
    player_hands = []
    for player in range(number_of_players):
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
    # Check to see if bag is empty
    if sum(bag.values()) == 0:
        return -2
    letter = choices(list(bag.keys()), weights=bag.values(), k=1)[0] 
    #while remove_letter_from_bag(letter, bag): #or bag.values().sum:
        #letter = choices(list(bag.keys()), weights=bag.values(), k=1)[0]
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

def play_round(player, hand, player_hands, scores, dictionary, letter_values, board, bag, first_go):
    if None in hand:
        hand = [letter for letter in hand if letter != None]
    print(f"\nPlayer {player}'s turn.\nScore: {scores[player]}\nHand: {' '.join(hand)}\n")
    words_to_test = [None] # Set to None so first instance of while loop doesn't error
    
    while are_words_in_dictionary(words_to_test, dictionary) == False:
        if words_to_test != None:
            proposed_word = input("Word: ")
            if proposed_word == '/pass':
                return -1
            proposed_location, proposed_direction = input("Start location: "), input("Word direction: ")
        
        while user_input_validity(proposed_word, proposed_location, proposed_direction, board, first_go, player_hands[player]) == False:
            proposed_word = input("Word: ")
            proposed_location, proposed_direction = input("Start location: "), input("Word direction: ")
            
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
        if add_letter_to_hand(player_hands, player, bag) == -1:
            return "Bag is empty! Use /pass to end the game"

    add_word_to_board(proposed_word, proposed_location, proposed_direction, board) 
    round_score = calculate_score(letter_values, words_to_test)
    scores[player] += round_score
    print(f"You scored {round_score} points!\n"), sleep(2), show_scrabble_board(board)
    first_go = 0