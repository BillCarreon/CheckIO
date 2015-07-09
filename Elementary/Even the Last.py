def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    #check for an empty array and return zero if true
    if len(array) <= 0:
        return 0
    #instantiate sum and product variables
    array_sum = 0 
    prod = 0
    #get index of last value in list
    last_idx = len(array)-1
    #get value of last item in list
    last_val = array[last_idx]
    #iterate through array, storing item index in idx and item value in val
    for idx, val in enumerate(array):
        #check to see if the index is an even number
        if idx%2 == 0:
            #if yes, add the value to sum
            array_sum += array[idx]
    #multiply the sum by the last value in the array
    prod = array_sum * last_val
    #return the product
    return prod

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
