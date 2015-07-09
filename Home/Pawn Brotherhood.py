"""
This module computes the number of save pawns.

"""

import string


NUM_ROWS = 8


# O(n)
def locs_to_coords(locs):
    """
    Args:
        locs: set
    """

    coords = []
    letter_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

    # O(n)
    for loc in locs:
        col = letter_dict[loc[0]]
        #row = NUM_ROWS - int(loc[1])
        # appends (row, col) tuple
        coords.append(( NUM_ROWS - int(loc[1]), letter_dict[loc[0]]))
    return coords


def coords_to_locs(coords):

    locs = []
    num_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
    #O(1)
    for coord in coords:
        # coord is a 2-tuple: (4, "b")
        row, col = coords
        locs.append(num_dict[col]]+str(8 - row))
        
    return locs


#O(1)
def getCheckCoords(pawn_coord):
    """
    [Description]
    
    Args:
        pawn_coord: (row, col) tuple
    """
    #TODO: check if these "coords" are within the bounds of the board
    #O(1)
    coord1 = [pawn_coord[0]+1, pawn_coord[1]-1]
    coord2 = [pawn_coord[0]+1, pawn_coord[1]+1]
    coords_to_check = []
    """balh"""
    #O(1)
    if 0 <= coord1[0] < 8 and 0 <= coord1[1] < 8 :
        coords_to_check.append(coord1)
    #O(1)
    if 0 <= coord2[0] < 8 and 0 <= coord2[1] < 8 :
        coords_to_check.append(coord2)
        
    return coords_to_check


def fucn(a, b, c):
    """
    [Description]
    
    Args:
        a: number of paws, int
        b: set of pawn locations
        c: ...
    
    Returns:
        The number os "safe" pawns (int)
    """
    pass


# O(1) + O(n) + O(n) -> O(n)
def safe_pawns(pawns):
    
    # O(1)
    counter_safe_pawns = 0

    # O(n)
    pawns_coords = locs_to_coords(pawns)
    # O(n)
    for pawn in pawns_coords:
        # O(1)
        check_coords = get_check_coords(pawn)
        # O(1)
        check_locs = coords_to_locs(check_coords)
        print('check_locs: '+str(check_locs))        
        
        # O(1)
        for loc in check_locs:
            # O(1)
            if loc in pawns:
                counter_safe_pawns += 1
                break

    return counter_safe_pawns


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns(["b4", "d4", "f4", "c3", "e3", "g5", "d2"]) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1