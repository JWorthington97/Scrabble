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

def are_words_in_dictionary(words_to_test, dictionary):
    for word in words_to_test:
        if word not in dictionary.keys():
            if word != None:
                print(f"{word} is not a word! - TESTING")
            return False
    return True

def calculate_score(letter_values, words_to_test): #multiplier
    round_score = 0
    for word in words_to_test:
        for char in word:
            round_score += letter_values[char]
    return round_score