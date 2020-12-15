import string as st

#   Create a list of the alphabet
alphabet = list(st.ascii_lowercase)

#   Create a blank dictionary to count   
dictionary = {i : 0 for i in alphabet}

#   Import Puzzle Input
with open("day06input.txt", "r") as file:
    answers = file.read().split("\n\n")
    groups = answers.copy()
    #   Now also split each group into individual people
    groups = [group.split("\n") for group in groups]


#   PART ONE 


#   Create a list to store the dictionaries containing the count of each persons answers
counts = []

#   Run through the answers and count the occurence of each letter
for answer in answers:
    count = dictionary.copy()
    for character in answer:
        if character in count.keys():
            count[character] += 1
        else:
            pass
    counts.append(count)

#   Count the number of questions answered by each group

questions = []
for count in counts:
    question = 0
    for letter in count.keys():
        if count[letter] != 0:
            question += 1
    questions.append(question)

#   Now sum the counts
sum = 0
for question in questions:
    sum += question



print("The solution to Part One is", sum)
    

#   PART TWO


#   Create a dictionary template to store the counts
dictionary = {i : 0 for i in alphabet}

#   For each group, its len is the number of people in the group
group_counts = []

for group in groups:
    group_count = []
    for person in group:
        person_count = dictionary.copy()
        for answer in person:
            if answer in person_count.keys():
                person_count[answer] += 1
        group_count.append(person_count)
    group_counts.append(group_count)

#   Now we need to check if each answer was answered by every person in each group
per_person_counts = []
for group in group_counts:
    per_person_count = 0
    group_count = dictionary.copy()
    n = len(group) # store how many group members there are

    for i in range(0, n):
        for letter in group[i].keys():
            if group[i][letter] > 0:
                group_count[letter] += 1

    for letter in group_count.keys():
        if group_count[letter] >= n: # if every person in the group answered that question
            per_person_count += 1
    
    per_person_counts.append(per_person_count)
        
#   Now count the sum
new_sum = 0

for group in per_person_counts:
    new_sum += group
    
print("The solution to Part Two is", new_sum)