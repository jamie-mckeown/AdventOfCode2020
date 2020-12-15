#   Import and Format Puzzle Input

with open("day02input.txt", "r") as file:
    lines = file.read().split("\n") # separate each password and condition into a unique line of lines

#   PART ONE

valid1 = 0

for line in lines: # for each password,...
    [condition, password] = line.split(":") # split the condition and password into separate list items
    [values, letter] = condition.split(" ") # splits the condition 1-3 a into [1-3, a]
    [lower, upper] = values.split("-") # splits the condition 1-3 into [1, 3]

    if int(lower) <= password.count(letter) <= int(upper): # if the password satisfies the conditions, its valid
        valid1 += 1 # add 1 to the number of valid passwords

print("The solution to Part One is", valid1) # the result is 474

#   PART TWO

valid2 = 0 

for line in lines: # for each password,...
    [condition, password] = line.split(": ") # split the condition and password into separate list items, making sure to remove spaces as they count as a character
    [values, letter] = condition.split(" ") # splits the condition 1-3 a into [1-3, a]
    [lower, upper] = values.split("-") # splits the condition 1-3 into [1, 3]

    lower = int(lower) - 1
    upper = int(upper) - 1 # change lower and upper to be indexes, not position

    if password[lower] == letter and password[upper] != letter:
        valid2 = valid2 + 1
    elif password[upper] == letter and password[lower] != letter:
        valid2 = valid2 + 1


print("The solution to Part Two is", valid2)