#   rules, my ticket and the other tickets are separated by a blank line, or equivalently \n\n
with open("day16input.txt", "r") as file:
    data = file.read().split("\n\n")

    rules_list = data[0].split("\n")
    my_ticket = data[1].split("\n")[1] # remove heading "your ticket:" 
    tickets = data[2].split("\n")[1:] # remove heading "nearby tickets" 

#   part one would be easier if each ticket was a list itself, and if the elements were integers
tickets = [ticket.split(",") for ticket in tickets]
for ticket in tickets:
    for i in range(len(ticket)):
        ticket[i] = int(ticket[i])

my_ticket = my_ticket.split(",")
for i in range(len(my_ticket)):
    my_ticket[i] = int(my_ticket[i])


#   part two will likely require we know which of the rules is for which field on the tickets
rules = {}
for rule in rules_list:
    field, ranges = rule.split(": ")
    ranges = ranges.split(" or ")
    
    a1, b1 = ranges[0].split("-")
    a2, b2 = ranges[1].split("-")
    a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)

    ranges = [(a1, b1), (a2, b2)]

    rules[field] = ranges


#   Part one function: check if values are in the given ranges
def fits_range(val):
    '''Takes a value and returns True if the value is inside one of the allowed ranges, otherwise False.'''
    fits = 0

    val = int(val)

    for ranges in rules.values():
        for lower, upper in ranges:
            if val in range(lower, upper+1):
                fits += 1

    return True if fits != 0 else False

#   Part one function: validate tickets
def valid_ticket(ticket):
    ''''''

    invalid = []

    for entry in ticket:
        if not fits_range(entry):
            invalid.append(entry)

    return (True, invalid) if len(invalid) == 0 else (False, invalid)

    
invalids = []

for ticket in tickets:
    if not valid_ticket(ticket)[0]:
        invalids.append(valid_ticket(ticket)[1])


sum = 0
for invalid in invalids:
    for fail in invalid:
        sum += int(fail)

print("The solution to Part One is", sum)


#   Part two

#   We are told to discard the failed tickets
tickets = [ticket for ticket in tickets if valid_ticket(ticket)[0]]

#   Include our ticket
tickets.append(my_ticket)

#   Create dictionary to store field:indexes such that the entries at those indexes in every list are valid for that field.
valid_indexes = {}

#   For every field, check each ticket against its ranges 
for field, ranges in rules.items():
    lower1, upper1, lower2, upper2 = ranges[0][0], ranges[0][1], ranges[1][0], ranges[1][1]
    valids = []
    
    for col in range(len(tickets[0])): # lets us select the same index in every ticket
        all = True
        for ticket in tickets:
            if (ticket[col] in range(lower1, upper1+1)) or (ticket[col] in range(lower2, upper2+2)):
                pass
            else:
                all = False

        if all:
            valids.append(col)

    valid_indexes[field] = valids 

# turns out num of valid indexes is distinct for each field, and ranges 1 - 20 inclusively covering all numbers - i.e. we can iterate over the length and track which ones we have already paired up to eliminate further possibilities 

del rules # will recycle this dictionary to store field:index when we find the correct indexes
rules = {} # del line probably unneeded


#   Will assume that, e.g., the length 20 list... ... length 3 list contains length 2 list contains the length 1 list, so that each time we choose a value, it immediately picks the others for us consequently

counted = []
for L in range(1, len(valid_indexes)+1): # for each length L from 1 to 20
    for field in valid_indexes.keys():
        if len(valid_indexes[field]) == L:
            for i in valid_indexes[field]:
                if i not in counted:
                    rules[field] = i
                    counted.append(i)
                

departure_indexes = []
#   Find departure fields in my ticket
for field in rules.keys():
    if field.startswith("departure"):
        departure_indexes.append(rules[field])


my_departures = []
for index in departure_indexes:
    my_departures.append(my_ticket[index])

prod = 1
for value in my_departures:
    prod *= value 

print("The solution to Part Two is", prod)




