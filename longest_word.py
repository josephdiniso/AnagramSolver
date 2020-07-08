from typing import List

def get_longest_words(allowed_string: str) -> List[str]:
        # Opens wordlist file and creates list of all words
        with open("wordlist.txt") as f:
            wordlist = []
            for line in f:
                wordlist.append(line.strip())
        allowed = [letter for letter in allowed_string]
        # List of usable words to be appended to
        word_list = []
        iter_var = 0
        for word in wordlist:
            allowed_list = allowed.copy()
            allowed_word = False
            # Iterates through every letter in each word
            for letter in word:
                # If word contains letter not in list, loop is broken and word is not allowed to be appended
                if letter not in allowed_list:
                    allowed_word = False
                    break
                else:
                    # If letter is in list, letter is removed from copy of list and word may be allowed to be appended
                    allowed_list.remove(letter)
                    allowed_word = True

            if allowed_word==True and len(word)>=3:
                word_list.append(word)

        word_list = sorted(word_list,key=len, reverse=True)
        return word_list
    
