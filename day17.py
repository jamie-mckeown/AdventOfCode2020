def get_3d_neighbours (origin) :
    '''Takes a point in 3D space given by (x,y,z) tuple coordinates and returns neighouring points - that is points that are within 1 step in any of the 3 directions x, y, z. len(neighbours) should always be 26 for the 3D case.'''
    range = [1, 0, -1] # the variations allowed from x, y and z.
    neighbours = []
    x, y, z = origin

    for xr in range:
        for yr in range:
            for zr in range:
                pt = (x + xr, y + yr, z + zr)

                if pt != (x, y, z):
                    neighbours.append(pt)

    return neighbours

#   Puzzle input gives points x, y, 0 and the choice is arbritrary so set top right corner to origin
with open("day17input.txt", "r") as file:
    data = file.read().split("\n") # first line is y=0, second is y=1, etc...

Active = []

for i in range(len(data[0])):
    for j in range(len(data)):
        if data[j][i] == "#":
            Active.append((i, j, 0))

#   Now the initial set of Active points is stored as a list of tuples

cycle = 0 # track which iteration we are at

while cycle != 6:
    cycle += 1 # first cycle is cycle 1 not cycle 0 - incrementing now makes sure we do the 6th run

    # what ranges of x,y,z do we need to consider each time?
    # each cycle adds 1 to each end of x and y (so changes the range by 2 for both)
    # each cycle adds 2 new z planes (at each end of z)
    # hence each time we check the edges +- 1, which compared to the original is +- cycle number?
    # and we need to consier THEIR neighbours, which are one further out so... cycle + 1 away from origin each time needs to be checked
    check = cycle + 1

    nowActive = []
    for x in range(0 - check, len(data[0]) + check):
        for y in range(0 - check, len(data) + check):
            for z in range(0 - check, 0 + check):
                neighbours = get_3d_neighbours((x, y, z)) # find the points neighbours
                
                count = 0 # count the number of active neighbours
                for pt in Active:
                    if pt in neighbours:
                        count += 1

                #   Follow rules to determine new active points
                if (x, y, z) in Active and (count == 2 or count ==3):
                    nowActive.append((x, y, z))
                elif (x, y, z) not in Active and count == 3:
                    nowActive.append((x, y, z))

    Active = nowActive # update the current active points for next cycle

print("The solution to Part One is", len(Active))
    
#   Part TWO

#   The problem is now 4 dimensional, so should still be doable with the same logic as above:
#   The 4th dimension will be spanned by t - little nod to relativity

def get_4d_neighbours ( origin ) :
    ''' Takes a point in 4D as a tuple origin = (x, y, z, t) and outputs a list of all points which have x,y,z,t coordinates within 1 space of the origin's. Neighbours should contain 80 elements.'''
    range = [-1, 0, 1]
    x, y, z, t = origin
    neighbours = []

    for xr in range:
        for yr in range:
            for zr in range:
                for tr in range:
                    pt = (x + xr, y + yr, z + zr, t + tr)

                    if pt != (x, y, z, t):
                        neighbours.append(pt)

    return neighbours


#   reset the problem
Active = []
for i in range(len(data[0])):
    for j in range(len(data)):
        if data[j][i] == "#":
            Active.append((i, j, 0, 0))

cycle = 0

print("Warning: Part two takes a long time to run!")
# # #   solve the 4d problem
while cycle != 6:
    cycle += 1
    print(cycle)
    check = cycle + 1

    nowActive = []
    for x in range(0-check, len(data[0])+check):
        for y in range(0-check, len(data)+check):
            for z in range(0-check, 0+check):
                for t in range(0-check, 0+check):
                    neighbours = get_4d_neighbours((x,y,z,t)) # get this points neighbouring points

                    count = 0
                    for pt in Active:
                        if pt in neighbours:
                            count += 1

                    #   follow the same rules as before for determing
                    if (x,y,z,t) in Active and (count == 2 or count == 3):
                        nowActive.append((x,y,z,t))
                    elif (x,y,z,t) not in Active and count == 3:
                        nowActive.append((x,y,z,t))

    Active = nowActive # update current active points for next cycle.


print("The solution to Part Two is", len(Active))