def index_power(array, n):
    #if n is larger than the array length, return '-1'
    if n >= len(array):
        return -1
    else:
        #set 'value_at_n' to the value at n
        value_at_n = array[n]
        #set 'value_at_n' to the ntn power
        nth_power = value_at_n**n
        #return the value at n to the nth power
        return nth_power

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"