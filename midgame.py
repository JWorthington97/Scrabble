from pregame import remove_letter_from_bag
def show_scrabble_board(board):
    print('  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O')
    # Need to align the top row with the board (e.g double digits too)
    row_index = 0
    for row in board:
        print(str(row_index) + ''.join(row))
        row_index += 1

def add_letter_to_hand():
    ""
    # Check if remove_letter_from_bag returns False
    #if so, choose another letter to remove
    #Copy pasted from pregame - cut these lines out of pregame and replace with add_letter_to_hand
    #letter = chr(randint(65,90))
        # When assigning letters in the midgame function, we will need to check whether remove_letter_from_bag returns True/False
    #    remove_letter_from_bag(letter, bag)