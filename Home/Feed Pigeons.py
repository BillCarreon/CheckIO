def checkio(number):
    minutes = 0
    numBirds = 0
    birdsFed = 0
    birds =  []
    print('--------------------')
    while True:
        minutes += 1
        for x in range(minutes):
            birds.append(0)
        for x in range(len(birds)):
            if number > 0: 
                birds[x] += 1
                number -= 1
        print(len(birds))
        if number == 0:
            break
    for x in birds:
        if x > 0:  
            birdsFed += 1       
    
    return birdsFed

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"