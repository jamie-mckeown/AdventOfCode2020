#   Import and format the puzzle data

with open("day01input.txt", "r") as file:
    numbers = file.read() # imports the data as a single string
    numbers = numbers.split("\n") # convert this string into a list of the individual strings for each number
    ints = [int(number) for number in numbers]

#   PART ONE

pairs = [] # empty list to store pairs that sum to 2020
products = [] # empty list to store the products of pairs that sum to 2020

for a in ints:
    for b in ints:
        if a + b == 2020:
            pairs.append([a,b])
            products.append(a*b)
            
print("The solution to Part 1 is", products[0]) # The product is 935419

#   PART TWO

triples = []
products = []

for a in ints:
    for b in ints:
        for c in ints:
            if a + b + c == 2020:
                triples.append([a,b,c])
                products.append(a*b*c)


print("The solution to Part 2 is", products[0]) # the product is 49880012