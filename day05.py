#   Import the data as a string, split it into a list of tickets, then split each ticket into a row instruction and a column instruction
with open("day05input.txt", "r") as file:
    tickets = file.read().split("\n")
    tickets = [[ticket[:-3], ticket[-3:]] for ticket in tickets] # [row instruction, column instuction]

#   PART ONE


seat_ids = [] 

for ticket in tickets:
    row = [0, 127]  #   Intial range of rows to consider
    col = [0, 7] #   Initial range of columns to consider

    while (row[1]-row[0]) > 0:
        for direction in ticket[0]:
            row_mid = (row[1] - row[0]) / 2
            
            if row_mid.is_integer():
                row_mid = row_mid
            else:
                row_mid += 0.5

            row_mid = row_mid + row[0] # scale it into the correct interval

            if direction == "F":
                row = [row[0], row_mid - 1]
            else:
                row = [row_mid, row[1]]
    
    row = int(row[0])  

    while (col[1] - col[0]) > 0:
        for direction in ticket[1]:
            col_mid = (col[1] - col[0]) / 2

            if col_mid.is_integer():
                col_mid = col_mid
            else:
                col_mid += 0.5

            col_mid = col_mid + col[0]

            if direction == "L":
                col = [col[0], col_mid-1]
            else:
                col = [col_mid, col[1]]

    col = int(col[0])

    seat_ids.append(8*row + col)    


#   Now we have a list of seat ids we need the largest, so sort it and take the last index
seat_ids.sort()

print("The solution to Part 1 is {}".format(seat_ids[-1]))


#   PART TWO

for i in range(48,818): # we dont need to check the last seat anyway
    if i+1 not in seat_ids: # if the seat id is missing, its ours!
        print("The solution to Part Two is {}".format(i+1))
    else:
        pass