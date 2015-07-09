def count_neighbours(grid, row, col):    

    my_loc = (col, row)
    N  = [col, row-1]
    S  = [col, row+1]
    E  = [col+1, row]
    W  = [col-1, row]
    NE = [E[0],N[1]]
    SE = [E[0],S[1]]
    SW = [W[0],S[1]]
    NW = [W[0],N[1]]   
    neighbors = (N,S,E,W,NE,SE,SW,NW)       
    sum_neighbors = 0
    
    for x,y in neighbors:
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            if grid[y][x] == 1:
                sum_neighbors += 1

    return sum_neighbors


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
