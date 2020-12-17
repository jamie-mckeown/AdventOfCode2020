#   Functions to convert from decimal to binary and back.
def base_change (num, old_base, new_base):
    '''Takes a number num in base old_base and converts it into base new_base by first converting it to decimal. Outputs an integer in base new_base.'''
    
    a = old_base
    b = new_base
    n = num

    # convert num to from base a to base 10 if not already
    if a == 10:
        dec = str(n)
    else:
        digits = list(str(n))
        digits.reverse() # so index 0 is the 0th power of a, etc...
        
        dec = 0
        for i in range(len(digits)):
            dec += int(digits[i]) * (a**i)

    n = int(dec)

    #   convert base 10 into base b
    if b != 10:
        new_digits = []

        while n != 0:
            digit = n % b # the digit is the remainder when dividing by mod b
            # print(digit)
            new_digits.append(digit) # store the digit, then rescale n
            n = n // b # this returns essentially n/b - remainder to give the nearest whole number
            # print(n)

        new_digits.reverse() # put digits in the correct order

        #   create a string out of the list
        n = ''
        for digit in new_digits:
            n = n + str(digit)

    return int(n)

def decimal_to_binary (num):
    return str(base_change(num, 10, 2))

def binary_to_decimal (num) :
    return str(base_change(num, 2, 10))


#   Functions to convert standard binary into 36 bit binary and back
def bit_36 (num, bits=36) :
    '''Takes a binary number written as a string and converts it into a 36 bit binary string (by appending an appropriate amount of zeros'''

    length = len(str(num)) # how many digits the number has already
    diff = bits - length # the number of 0s required to be appending to the front

    zeros = diff * "0" # produces 00000... diff times

    n = zeros + str(num)

    return n

def bit_36_rm (num) :
    '''Takes a 32 bit binary number and removes leading zeros (or ignores the 36 bit requirement).'''

    n = str(num)

    while n.startswith("0"):
        n = n[1:]

    return n


#   Get puzzle input
with open("day14input.txt", "r") as file:
    data = file.read().split("\n")


#   For each of the instructions we need to check if its a mask or a mem. if its mask, update mask with the new mask and proceed, otherwise we need to convert, mask and then store the information provided.

mask = '' # immediately changed when we initalise the method
mem = {}  # this will be filled, and overwritten with the memory address as key and the masked converted value as value

for line in data:
    if "mask" in line:
        mask = str(line.split(" = ")[1])
    elif "mem" in line:
        pos = int(line.split(" = ")[0][4:-1]) # takes x from mem[x] and converts it into a number
        val = line.split(" = ")[1]

        # convert val into 32 bit binary
        pos_36 = bit_36(decimal_to_binary(val))

        # apply the mask
        masked_val = ' '
        for i in range(len(mask)):
            if mask[i] != "X":
                masked_val = masked_val + mask[i]
            else:
                masked_val = masked_val + pos_36[i]

        # convert back from 36 bit number to a decimal number
        masked_val = binary_to_decimal(int(bit_36_rm(masked_val)))
        
        # convert masked_val from a str to an int
        masked_val = int(masked_val)

        # store the value in memory
        mem[pos] = masked_val

sum_values1 = 0
for value in mem.values():
    sum_values1 += int(value)

print("The solution to Part One is", sum_values1)

#   Part Two

#   Now the bit mask will change the memory addresses, and actually assign the same value to a variety of different memory addresses
#   We might have to use recursion

def get_possible_outputs (masked_val):
    '''Takes a 36 bit masked binary string, replaces X's with all possible combinations of 0 and 1 and outputs all possible output values as a list.'''

    masked_val = str(masked_val) # this is almost surely unneeded but you never know!
    # poss_outputs = [] # this returns a list of lists of lists of lists... which is too messy to deal with
    poss_outputs = ''

    #   base case of recursion first - all the X's have been removed already
    if "X" not in masked_val:
        return masked_val
    else:
        loc = masked_val.index("X") # locates the first index that X appears at (left to right)

        poss0 = get_possible_outputs(masked_val[:loc] + "0" + masked_val[loc+1:])
        poss1 = get_possible_outputs(masked_val[:loc] + "1" + masked_val[loc+1:])

        poss_outputs = poss_outputs + "\n" + poss0
        poss_outputs = poss_outputs + "\n" + poss1

        return poss_outputs

# print(get_possible_outputs("1X"))
# print(get_possible_outputs("XX1"))

mask = ''
mem = {}

for line in data:
    if "mask" in line:
        mask = str(line.split(" = ")[1])
    elif "mem" in line:
        pos = int(line.split(" = ")[0][4:-1]) # takes x from mem[x] and converts it into a number
        val = line.split(" = ")[1]

        # convert pos into 36 bit binary
        pos_36 = bit_36(decimal_to_binary(pos))

        # apply mask to post_36
        masked_pos = ''
        for i in range(len(mask)):
            if mask[i] == "0":
                masked_pos = masked_pos + pos_36[i]
            else:
                masked_pos = masked_pos + mask[i]
            
        
        # masked_pos represents many possible memory addresses based on changing Xs into 0s and/or 1s
        poss_outputs_messy = get_possible_outputs(masked_pos) # has empty lines in it that need cleaned out

        possible = poss_outputs_messy.split("\n")

        possible = [bit_36_rm(poss) for poss in possible if poss != "\n" and poss != ""]
        possible = [binary_to_decimal(poss) for poss in possible]

        for poss in possible:
            mem[poss] = int(val)
  
sum_values2 = 0

for num in mem.values():
    sum_values2 += num

print("The solution to Part Two is", sum_values2)