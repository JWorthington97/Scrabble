from copy import deepcopy
# function initialises an empty board array
def create_scrabble_board():
    # double spaces here because of the 2*
    array = []
    for i in range(15):
        array.append([' ']*15)
    return array

def show_scrabble_board(board):
    print('    A B C D E F G H I J K L M N O')
    # Need to align the top row with the board (e.g double digits too)
    row_index = 0
    for row in board:
        if row_index < 10:
           y = ' ' + str(row_index) + '  '
        else:
            y = str(row_index) + '  '
        
        print(str(y) + ' '.join(row))
        row_index += 1

def add_word_to_board(proposed_word, proposed_location, proposed_direction, board):
    #word has already been checked
    #word checks 
    word = proposed_word.upper().strip()
    if word.isalpha() == False:
        return -1 # Word contains non-alpha characters
    #location checks
    proposed_location = proposed_location.strip()
    if int(proposed_location[1::]) < 0 or int(proposed_location[1::]) > 14:
        return -2 # Out of row bounds
    if proposed_location[0].upper() < 'A' or proposed_location[0].upper() > 'O':
        return -2 # Out of column bounds
    #direction checks
    direction = proposed_direction.upper().strip()
    if direction not in ['R', 'D',  'RIGHT', 'DOWN']:
        return -3 # Invalid direction

    #convert character into integer
    column = ord(proposed_location[0]) - 65 # ASCII value for 'A'
    row = int(proposed_location[1::])
    if direction in ['R', 'RIGHT']:
        if column + len(word) >= 16:
            return -4 # Word would exceed column bounds (i.e. past O)
        else:
            for index, letter in enumerate(word):
                board[row][column + index] = letter
    else:
        if row + len(word) >= 16:
            return -4 # Word would exceed row bounds (i.e. past 14)
        else:
            for index, letter in enumerate(word):
                board[row + index][column] = letter
    return 0

#down checks
def get_words_from_board_down(proposed_word, start_location, board):
    words_to_test = []
    words_to_test.append(proposed_word)
    in_function_board = deepcopy(board)
    add_word_to_board(proposed_word, start_location, 'D', in_function_board)
    # We need to add this to convert the user provided start location (e.g. 'H6') to the row and column indices for the board (e.g. 6,7)
    start_location = [int(start_location[1::]), ord(start_location[0]) - 65]

    for index in range(-1, len(proposed_word) + 1):
        on_board_word_start = [start_location[0] + index, start_location[1]] #Offsets for whatever row we are now on
        on_board_word_end = [start_location[0] + index, start_location[1]]

        #checking left
        while in_function_board[on_board_word_start[0]][on_board_word_start[1] - 1] != ' ' and on_board_word_start[1] - 1 >= 0:
            on_board_word_start[1] -= 1
        
        #checking right
        while on_board_word_end[1] + 1 < 15 and in_function_board[on_board_word_end[0]][on_board_word_end[1] + 1] != ' ':
            on_board_word_end[1] += 1
            
        # append word to the words_to_test array
        string = ""
        for i in range(on_board_word_start[1], on_board_word_end[1] + 1):
            string += in_function_board[on_board_word_start[0]][i]
        if len(string) > 1:
            words_to_test.append(str(string))
    return words_to_test

# right checks
def get_words_from_board_right(proposed_word, start_location, board): 
    words_to_test = []
    words_to_test.append(proposed_word)
    in_function_board = deepcopy(board)
    add_word_to_board(proposed_word, start_location, 'R', in_function_board) 
    start_location = [int(start_location[1::]), ord(start_location[0]) - 65]
    
    for index in range(-1, len(proposed_word) + 1):
    #for index, letter in enumerate(proposed_word):
        #print("LETTER: " + letter)
        on_board_word_start = [start_location[0], start_location[1] + index]
        on_board_word_end = [start_location[0], start_location[1] + index]

        #checking up
        while in_function_board[on_board_word_start[0] - 1][on_board_word_start[1]] != ' ' and on_board_word_start[0] - 1 >= 0:
            on_board_word_start[0] -= 1
        
        #checking down
        while on_board_word_end[0] + 1 < 15 and in_function_board[on_board_word_end[0] + 1][on_board_word_end[1]] != ' ':
            on_board_word_end[0] += 1
            
        # append word to the words_to_test array
        string = ""
        for i in range(on_board_word_start[0], on_board_word_end[0] + 1):
            string += in_function_board[i][on_board_word_start[1]]
        if len(string) > 1:
            words_to_test.append(str(string))
    return words_to_test