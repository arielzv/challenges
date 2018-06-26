from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    f = open("dictionary.txt")
    content = f.readlines()
    f.close()
    
    return [word.strip() for word in content]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word = word.replace("-","")
    value = sum([LETTER_SCORES[letter.upper()] for letter in word])
    return value

def max_word_value(words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    max_word = ""
    for word in words:
        value = calc_word_value(word)
        if value>max_value:
            max_value = value
            max_word = word

    return max_word


        
if __name__ == "__main__":
    pass # run unittests to validate
