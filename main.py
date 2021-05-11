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

board[6][8] = 'O'
board[6][9] = 'V'
board[6][10] = 'E'

board[8][5] = 'S'
board[8][6] = 'A'

board[3][6] = 'T'

# board[7][8] = 'T'
# board[8][8] = 'H'
# board[9][8] = 'E'
# board[10][8] = 'R'

#show_scrabble_board(board)

# receive word, location, direction
# find all the collisions on the board, and save them all as words
# check all of the words
#if ONE is not a word, can't put the received word down
# 6              L O V E
# 7              E T
# 8          S A M H
# 9              O E
#10              N R

#function to get array of collision words
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

#test_words = []
#test_words.append(proposed_word)
#going down each row
#for row in word:
    #word_on_board_start = [row,column]
    #word_on_board_end = [row,column]
    # checking left of the character in the word
    #while board[row][column -1] != None or */^ or out of bounds:
        #word_start = [row,column -1]
    #checking right of character in the word
    #while board[row][column + 1] != None or */^ or out of bounds:
        # word_end = [row][column + 1]
    #if word_start[1] = word_start[0] != 1:
        #test_words.append(word) 

words_to_test = []
words_to_test.append(proposed_word)
start_location = [6,8] # = 'I6'
# they provide the whole word e.g OTHER
# if down:
#   if board[row][column] == proposed_word[0] #this means that they want the word to start with O, and so we don't remove it from their hand
#      remove_from_hand
#   if board[row + len(word)][column] == proposed_word[-1]:
#       they want to join on the last letter in the word

#down checks
for index, letter in enumerate(proposed_word):
    #print("LETTER: " + letter)
    on_board_word_start = [start_location[0] + index, start_location[1]] #Offsets for whatever row we are now on
    on_board_word_end = [start_location[0] + index, start_location[1]]

    #checking left
    while board[on_board_word_start[0]][on_board_word_start[1] - 1] != ' ':
        on_board_word_start[1] -= 1
    
    #checking right
    while board[on_board_word_end[0]][on_board_word_end[1] + 1] != ' ':
        on_board_word_end[1] += 1
        
    # append word to the words_to_test array
    string = ""
    for i in range(on_board_word_start[1], on_board_word_end[1] + 1):
        string += board[on_board_word_start[0]][i]
    words_to_test.append(str(string))
print(words_to_test)

# We need to check above and below the start and end index
# Figuring out where they are joining onto the board and then do NOT subtract from the hand
            



