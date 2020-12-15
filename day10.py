with open("day10input.txt") as file:
    data = file.read().split("\n")
    data = [int(number) for number in data]
    data.sort()

outlet = 0
device = data[-1] + 3

#   Add charging port and device to the list of adapters
data = [outlet] + data + [device]


# Check the given order of adapters is valid
def valid_differences () :
    ''' Returns True if adjacent adapters are 1, 2 or 3 jolts different from each other, and False otherwise.'''

    valid = [1, 2, 3]
    fails = 0 
    for i in range (len(data) - 1) :
        diff = data[i+1] - data[i]

        if diff not in valid:
            fails += 1
            break
        
    return True if fails == 0 else False
        



def get_joltage_diff () :
    count1 = 0 # 1 jolt differences
    count2 = 0 # 2 jolt differences
    count3 = 0 # 3 jolt differences


    for i in range(len(data) - 1) :
        diff = data[i+1] - data[i]
        if diff == 1:
            count1 += 1
        elif diff == 2:
            count2 += 1
        elif diff == 3:
            count3 += 1

    return count1, count2, count3


count1, count2, count3 = get_joltage_diff()

print("The solution to Part One is", count1 * count3)

#   PART TWO    #

# print(data)

checked_indexes = {} # to stop us from checking all trillion possibilities
def get_num_arrangements (index) :

    if index == len(data) - 1 : # if we are at the last index, terminate
        return 1 # there is only 1 possible route after - our device!

    count = 0

    if index in checked_indexes.keys():
        return checked_indexes[index]


    for i in range(index + 1, len(data)) : # index + 3 throws an IndexError, since data is ordered, everything afer index+3 is ignored.
        if data[i] - data[index] <= 3 :
            count = count + get_num_arrangements(i)



    checked_indexes[index] = count
    return count


    
print("The solution to Part Two is", get_num_arrangements(0))

