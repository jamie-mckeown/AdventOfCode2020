#   Import and format puzzle input

with open("day03input.txt", "r") as file:
    trees = file.read().split("\n") # splits the trees into rows
    last_spot = len(trees[0]) # after which the rows start repeating
    last_row = len(trees) # last row of the forest

#   PART ONE    #

tobbogan = trees[0][0]

#   Variable to store the number of encountered trees
hits1 = 0

#   Let's use index i for the rows of trees, and j for the columns
i = 0 # when i = 323 we are done
j = 0 # when j = 31 we should set j to 0 immediately.

while i < last_row:
    tobbogan = trees[i][j % last_spot] # is the tobbogan on a blank space or a tree
    if tobbogan == "#":
        hits1 += 1 # if we have hit a tree, store it as a tree hit
    i += 1  #   Move 1 space down
    j += 3  #   Move 3 spaces across


print("The solution to Part One is", hits1)

#   PART TWO

#   We need to check the same as part 1 for different slopes (increments of i and j), so we will define a function that performs part 1 and repeat it for each of the different slopes

#   Save the slopes as a list
slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]



#   Function that computes the number of tree hits on a single slope.
def tree_count(slope):
    toboggan = trees[0][0]
    hits = 0

    i = 0
    j = 0

    while i < last_row:
        tobbogan = trees[i][j % last_spot] # is the tobbogan on a blank space or a tree
        if tobbogan == "#":
            hits += 1 # if we have hit a tree, store it as a tree hit
        i += slope[0] 
        j += slope[1]

    return hits

#   Define a variable to compute the product
prod = 1

#   Store the hits for me to check
hits2 = []

#   For each of the slopes, count the tree hits and then calculate the required product
for slope in slopes:
    local_hits = tree_count(slope)
    prod = prod*local_hits
    hits2.append(local_hits)

print("The solution to Part Two is", prod)

