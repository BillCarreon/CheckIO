import unicodedata

def checkio(words):
    
    word_list = words.split()
    sequence_counter = 0
    for word in word_list:
        if word.isdigit():
            sequence_counter = 0
        else:
            sequence_counter += 1
        if sequence_counter == 3:
            return True
            
    return False


if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
