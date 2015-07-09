import math

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


#input: a number between 0 and 99
#output: an array with the number names
def tens(number):
    num_name = []
    ones = number%10
    tens = math.floor(number/10)
    if number > 10 and number < 20:
        num_name.append(SECOND_TEN[number-10])
    else:
        if tens > 0: num_name.append(OTHER_TENS[tens])
        if ones > 0: num_name.append(FIRST_TEN[ones])
    return num_name

#input: a number between 0 and 999
#output: an array with the number names
def hundreds(number):
    num_name = []
    hundreds = math.floor(number/100)
    if hundreds > 0:
        num_name.append(FIRST_TEN[hundreds])
        num_name.append(HUNDRED)
    num_name += tens(number%100)
    
    return num_name
    
    
def thousands(number):
    num_name = []
    thousands = math.floor(number/1000)
    if thousands > 0:
        num_name.append(FIRST_TEN[thousands])
        num_name.append("thousands")
    num_name += hundreds(number%1000)
        

def checkio(number):
    if number == 0: return "zero"
    num_name = hundreds(number)

    #replace this for solution
    num_name = " ".join(num_name)
    return num_name


#Some hints
#Don't forget strip whitespaces at the end of string


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
