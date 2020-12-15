import numpy as np

with open("day09input.txt", "r") as file :
    data = file.read().split("\n") # import data from the text file and split at new line
    data = [ int(dat) for dat in data] # convert into a list of integers
    data = np.array(data) # convert the list of integers into a numpy array for speed.

def validity (number, preamble=[]) :
    ''' Takes an integer "number" as input and checks if number is the sum of two distinct integers in "preamble". '''
    valid_sums = []

    for a in preamble :
        for b in preamble :
            if a != b :
                valid_sums.append(a + b)

    if number in valid_sums :
        return True
    else:
        return False

i = 24  # indexing variable, initial index will be 24 + 1 = 25 as the first preamble is positions 0-24 inclusive.
valid = True # to record the first number that isnt the sum of distinct numbers from the previous 25
number = 0 # not necessary, just to get VSCode to stop complaining about potentially unbound values

while valid: # while failed = False
    i = i + 1
    
    number = data[i]
    preamble = data[i-25 : i]
    
    valid = validity(number, preamble) # if failed is true this will break the list

failed_number = number
print(f"The solution to Part One is {failed_number}.")


#   PART TWO    #

def continguous (number, data, step) :
    found = False
    set = []


    for i in range(len(data)-step) :
        set = data[i:i+step]
            
        if set.sum() == number :
            found = True
            return found, set
    
    return found, set


for step in range(2, len(data)) : # step size can not exceed the length of the dataset
    if continguous(number, data, step)[0] : # if we have found such a set
        result, contset = continguous(number, data, step)
        contset.sort()  # numpy arrays are sorted in place
        min_val = contset[0]
        max_val = contset[-1]
        print("The solution to Part Two is", min_val + max_val)
        break













