def checkio(text):
    alph = []
    text=text.lower()
    mostLet = 0
    mostNum = -1
    
    for x in range(26):
        alph.append(0)    
    for x in text:
        shitface = ord(x)-97
        if 0 <= shitface <= 25:
            alph[ord(x)-97]+=1
    for i,x in enumerate(alph):
        if x > mostNum:
            mostLet = i
            mostNum = x

    return chr(mostLet+97)


if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
