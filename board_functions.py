# function initialises an empty board array
def create_scrabble_board():
    # double spaces here because of the 2*
    array = []
    for i in range(15):
        array.append(['   ']*15)
    return array

def show_scrabble_board(board):
    print('A  B  C  D  E  F  G  H  I  J  K  L  M  N  O')
    # Need to align the top row with the board (e.g double digits too)
    row_index = 0
    for row in board:
       # print(row)
        #print(str(row_index) + ''.join(row))
        row_index += 1