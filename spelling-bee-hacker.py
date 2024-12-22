# NYTimes Spelling Bee Hacker
# Writte by: Myrela Bauman
# Date: 12/21/2024
# input file from: https://github.com/dwyl/english-words/tree/master

def load_words():
    with open('C:/Users/mybauman/Projects/misc/words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def find_words(letters, english_words):
    """
    Find all words that can be formed with the given letters.
    
    Rules:
    1. The first letter of the 'letters' string must be present
    2. The word must use a combination of the provided letters, but not all letters need to be used (except for the first)
    3. The word should not include any letters that are not in the provided list
    4. The word must be at least 4 letters long
    
    Params:
    - letters (str): A string of letters (user-defined). The first letter is the required letter.
    - english_words (set): The input set of words to loop through.

    Example:
    letters = "uocednf"
    found_words = ['ounce', 'confounded', 'fondue', ...]
    """

    letters = letters.lower()
    # extract first letter
    first_letter = letters[0]
    # create a set from the letters
    letter_set = set(letters)
    
    valid_words = []
    for word in english_words:
        # check if 1) word uses only the given letters, 2) includes the first letter, 3) does not contain any other letters not in the set
        if set(word).issubset(letter_set) and first_letter in word and len(word) >= 4:
            # append if all conditions are met
            valid_words.append(word)

    # sort alphabetically
    valid_words.sort()
    return valid_words


if __name__ == '__main__':
    english_words = load_words()

    ###### enter string of letters here. first letter is the required letter:
    letters = "uocednf" 
    ######

    found_words = find_words(letters, english_words)
    # print one word per line + total count
    for word in found_words:
        print(word)
    print(f"Total words found: {len(found_words)}")

    # QA step: check if specific word exists
    #print('stoic' in english_words)

