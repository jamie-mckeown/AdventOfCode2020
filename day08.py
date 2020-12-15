with open("day08input.txt", "r") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

n = len(data)

def find_accumulator_at_terminate (data) :
    accumulator = 0
    visited_indexes = []
    
    i = 0 # initial index is 0, i will index over the data

    while i not in visited_indexes:
        instruction = data[i]
        visited_indexes.append(i)

        if instruction.startswith("nop"):
            i += 1
        elif instruction.startswith("acc"):
            accumulator += int(instruction.split()[1])
            i += 1
        elif instruction.startswith("jmp"):
            i += int(instruction.split()[1])

    return accumulator

print("The solution to Part One is", find_accumulator_at_terminate(data))


#   PART TWO    #

def find_accumulator_at_terminate_end (data) :
    accumulator = 0
    visited_indexes = []
    
    i = 0 # initial index is 0, i will index over the data

    while i not in visited_indexes:
        instruction = data[i]
        visited_indexes.append(i)

        if instruction.startswith("nop"):
            i += 1
        elif instruction.startswith("acc"):
            accumulator += int(instruction.split()[1])
            i += 1
        elif instruction.startswith("jmp"):
            i += int(instruction.split()[1])

        if i >= n :
            return accumulator, True

    return accumulator, False


answer = 0
for j in range(n) :
    if data[j].startswith("nop") :
        data[j] = data[j].replace("nop", "jmp")

        acc, parity = find_accumulator_at_terminate_end(data) 

        if parity:
            answer = acc
            break
        else:
            data[j] = data[j].replace("jmp","nop")

    elif data[j].startswith("jmp") :
        data[j] = data[j].replace("jmp","nop")

        acc, parity = find_accumulator_at_terminate_end(data) 

        if parity:
            answer = acc
            break
        else:
            data[j] = data[j].replace("nop", "jmp")

print("The solution to Part Two is", answer)

