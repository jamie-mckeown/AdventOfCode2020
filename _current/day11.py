import numpy

with open("day11input.txt", "r") as file :
    data = file.read().split("\n")
    
    num_rows = len(data)
    num_cols = len(data[0])

    initial = numpy.zeros(shape=(num_rows, num_cols), dtype=int)
    
    #   Convert floor seats (.) into 0, unoccupied (L) into 1, and occupied (#) into 2
    keys = { "." : 0, "L" : 1, "#" : 2 }

    for i in range(num_rows) :
        for j in range(num_cols) :
            initial[i][j] = keys[data[i][j]]

def get_adjacent (row, col, current) :
    '''Takes a seat given by its row and column indexes, and returns a list of indexes for adjacent seats (within one space of it).'''
    neighbours = []

    #   Check if near edges
    if row == 0:
        row_min = row
        row_max = row + 1
    elif row == num_rows - 1:
        row_min = row - 1
        row_max = row
    else:
        row_min = row - 1
        row_max = row + 1

    if col == 0:
        col_min = col
        col_max = col + 1
    elif col == num_cols - 1:
        col_min = col - 1
        col_max = col
    else:
        col_min = col - 1
        col_max = col + 1

    
    for i in range(row_min, row_max + 1):
        for j in range(col_min, col_max + 1):
                if i == row and j == col:
                    pass
                else:
                    neighbours.append(current[i,j])

    return neighbours


previous = initial.copy()  
current = numpy.zeros_like(previous)

while not numpy.array_equal(current, previous):

    for i in range(num_rows) :
        for j in range(num_cols) :
            if (previous[i, j] == 1) and (2 not in get_adjacent(i,j,previous)):
                current[i, j] = 2
            elif (previous[i, j] == 2) and (get_adjacent(i,j,previous).count(2) >= 4):
                current[i, j] = 1
            else:
                current[i,j] = previous[i, j]

    if numpy.array_equal(current, previous) :
        break
    else:
        previous = current.copy()
        current = numpy.zeros_like(previous)


#   Now we count the number of occupied (2)

count = 0
for i in range(num_rows):
    for j in range(num_cols):
        if current[i,j] == 2:
            count +=1

print("The solution to Part One is", count)
   


#   PART TWO    #



#   New function to find 'adjacent' seats based on the new rule
def get_neighbours (row, col, current):
    ''' Takes a seat = (row, col) in the seating plan, and for each of compass directions away from it, finds the first seat (1 or 2) and stores what it is.'''
    
    
    neighbours = []
    n = row - 1 # up index
    s = row + 1 # down index
    e = col + 1 # right index
    w = col - 1 # left index

    # e.g. north east (up right) will be determined by both the n and e coordinate

    #   Booleans to check when we have checked all directions
    N, NE, E, SE, S, SW, W, NW = False, False, False, False, False, False, False, False # havent checked any direction yet

    while not (N and NE and E and SE and S and SW and W and NW):
        #   NORTH
        if not N and n >= 0: # row 0 is top row, therefore max up and only do so until weve checked all (and N = True)
            if current[n][col] == 2 or current[n][col] == 1:
                neighbours.append(current[n][col])
                N = True
        else:
            N = True

        #   NORTH-EAST
        if not NE and n >= 0 and e <= num_cols-1:
            if current[n][e] == 2 or current[n][e] == 1:
                neighbours.append(current[n][e])
                NE = True
        else:
            NE = True

        #   EAST
        if not E and e <= num_cols-1:
            if current[row][e] == 2 or current[row][e] == 1:
                neighbours.append(current[row][e])
                E = True
        else:
            E = True

        #   SOUTH EAST
        if not SE and e <= num_cols-1 and s <= num_rows - 1:
            if current[s][e] == 2 or current[s][e] == 1:
                neighbours.append(current[s][e])
                SE = True
        else:
            SE = True 

        #   SOUTH
        if not S and s <= num_rows-1:
            if current[s][col] == 2 or current[s][col] == 1:
                neighbours.append(current[s][col])
                S = True
        else:
            S = True 

        #   SOUTH WEST
        if not SW and s <= num_rows-1 and w >= 0:
            if current[s][w] == 2 or current[s][w] == 1:
                neighbours.append(current[s][w])
                SW = True
        else:
            SW = True 

        #   WEST
        if not W and w >= 0:
            if current[row][w] == 2 or current[row][w] == 1:
                neighbours.append(current[row][w])
                W = True
        else:
            W = True
        
        #   NORTH WEST
        if not NW and w >= 0 and n >= 0:
            if current[n][w] == 2 or current[n][w] == 1:
                neighbours.append(current[n][w])
                NW = True
        else:
            NW = True 

        #   And then move to the next lot to check
        n -= 1 # check one up
        s += 1 # check one down
        e += 1 # check one right
        w -= 1 # check one left

    return neighbours.count(2) # having issues with returning the list and then checking later

#   Reset the problem - arrays dont seem to be working anymore
previous = initial.copy()  
current = numpy.zeros_like(previous)


while not numpy.array_equal(previous, current):
    for i in range(num_rows) :
        for j in range(num_cols) :
            if (previous[i, j] == 1) and get_neighbours(i,j,previous) < 1:
                current[i, j] = 2
            elif (previous[i, j] == 2) and get_neighbours(i,j,previous) >= 5: # higher tolerance for num of people around
                current[i, j] = 1
            else:
                current[i,j] = previous[i, j]

    if numpy.array_equal(current, previous) :
        break
    else:
        previous = current.copy()
        current = numpy.zeros_like(previous)

count = 0
for i in range(num_rows):
    for j in range(num_cols):
        if current[i,j] == 2:
            count +=1

print("The solution to Part Two is", count)