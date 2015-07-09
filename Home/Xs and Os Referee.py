def checkio(game_result):
    counter = 0
    
#for loop to iterate through the given strings and replace them with game_results as nested arrays
    for indx,val in enumerate(game_result):
#this checks for the horizonal win
        if val == "XXX": return "X"
        if val == "OOO": return "O"
        game_result[indx] = list(val)
        
#this checks for diagonal NW to SE win
    if all([game_result[0][0]=="X",game_result[1][1]=="X",game_result[2][2]=="X"]): return "X"
    if all([game_result[0][0]=="O",game_result[1][1]=="O",game_result[2][2]=="O"]): return "O"
#this checks for diagonal NW to SE win
    if all([game_result[0][2]=="X",game_result[1][1]=="X",game_result[2][0]=="X"]): return "X"
    if all([game_result[0][2]=="O",game_result[1][1]=="O",game_result[2][0]=="O"]): return "O"

#loop to check the vertical win conditon
    while counter < 3:
#this checks for vertical win
        if all([game_result[0][counter]=="X",game_result[1][counter]=="X",game_result[2][counter]=="X"]): return "X"
        if all([game_result[0][counter]=="O",game_result[1][counter]=="O",game_result[2][counter]=="O"]): return "O"

        counter +=1
        
    else: return "D"
    return print("you should never see this")

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

