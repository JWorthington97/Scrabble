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

def add_word_to_board(proposed_word, proposed_location, proposed_direction,board):
    #word has already been checked
    #word checks 
    word = proposed_word.upper()
    if word.isalpha() == False:
        return -1 
    #location checks

    if int(proposed_location[1]) < 0 or int(proposed_location[1]) > 14:
        return -2
    if proposed_location[0].upper() < 'A' or proposed_location[0].upper() > 'O':
        return -2
    #direction checks
    direction = proposed_direction.upper()
    if direction not in ['R', 'D',  'RIGHT', 'DOWN']:
        return -3

    #convert character into integer
    column = ord(proposed_location[0]) - 65 # ASCII value for 'A' + 1 because of board quirks
    row = int(proposed_location[1])
    if direction in ['R', 'RIGHT']:
        if column + len(word) >= 16:
            return -4
        else:
            for index, letter in enumerate(word):
                board[row][column + index] = letter
    else:
        if row + len(word) >= 16:
            return -4
        else:
            for index, letter in enumerate(word):
                board[row + index][column] = letter
    return 0
    