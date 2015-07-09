def count_words(text, words):
    
    word_length = 0
    selection = text
    word_match_counter = 0
    
    for word in words:
        for _ in range(len(text)):    
            word_length = len(word)
            selection = text[_:_+word_length]
            if selection.lower() == word.lower():
                word_match_counter += 1
                break
        
    return word_match_counter


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
