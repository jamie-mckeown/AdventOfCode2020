#   PART ONE

#   Individual passports are separated by a single blank line
with open("day04input.txt", "r") as file:
    passports = file.read().split("\n\n")
    passports = [passport.replace("\n", " ") for passport in passports] # so passport data is only seprated by a space.
    passports = [passport.split(" ") for passport in passports] # Separate each passports data so we can access it

#   Convert individual passports into dictionaries and store those dictionaries in a list
dictionaries = []

for passport in passports:
    keys = []
    values = []
    for entry in passport:
        temp = entry.split(":")
        keys.append(temp[0])
        values.append(temp[1])
    dictionary = dict(zip(keys, values))
    dictionaries.append(dictionary)

passports = dictionaries # replace our old data with the easier to use data.

#   Define a function to check categories are present
def present(passport):
    '''Takes a passport as a dictionary and checks if the required entries are present. Returns True if the passport is valid and False otherwise.'''

    criterias = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    points = 0
    keys = passport.keys()

    for criteria in criterias[:-1]:
        if criteria in passport:
            points += 1

    return True if points == 7 else False


#   Create a variable to count the number of valid passports
valid = 0

for passport in passports:
    if present(passport):
        valid += 1

print("The number of valid passports is {}.".format(valid))
    

#   PART TWO
#   Import passport data and process it so that each passport is a dictionary, and we store the passports in a list
with open("day04input.txt", "r") as file:
    passports = file.read().split("\n\n")
    passports = [passport.replace("\n", " ") for passport in passports]
    passports = [passport.split(" ") for passport in passports]

    dictionaries = []

    for passport in passports:
        keys = []
        values = []
        for entry in passport:
            temp = entry.split(":")
            keys.append(temp[0])
            values.append(temp[1])
        dictionary = dict(zip(keys, values))
        dictionaries.append(dictionary)

    passports = dictionaries

#   Define a function to check a passport has birth year, and if the birth year is valid (4digits, 1920 to 2002)
def valid_byr(passport):
    if "byr" in passport.keys():
        if (len(passport["byr"]) == 4) and (1920 <= int(passport["byr"]) <= 2002):
            return True
        else:
            return False
    else:
        return False

#   Define a function to check a passport has issue year, and if the issue year is valid (4digits, 2010 to 2020)
def valid_iyr(passport):
    if "iyr" in passport.keys():
        if (len(passport["iyr"]) == 4) and (2010 <= int(passport["iyr"]) <= 2020):
            return True
        else:
            return False
    else:
        return False
    
#   Define a function to check a passport has expiration year, and if the expiration year is valid (4digits, 2020 to 2030)
def valid_eyr(passport):
    if "eyr" in passport.keys():
        if (len(passport["eyr"]) == 4) and (2020 <= int(passport["eyr"]) <= 2030):
            return True
        else:
            return False
    else:
        return False

#   Define a function to check the passport has height, and that the height is valid (a number followed by cm or in, that is 150 to 193 if in cm and 59 to 76 if in in)
def valid_hgt(passport):
    if "hgt" in passport.keys():
        if passport["hgt"].endswith("cm"):
            if 150 <= int(passport["hgt"][:-2]) <= 193:
                return True
            else:
                return False
        elif passport["hgt"].endswith("in"):
            if 59 <= int(passport["hgt"][:-2]) <= 76:
                return True
            else:
                return False
    else:
        return False

#   Define a function to check the passport has a hcl entry, and if the hcl is valid (starts with # followed b exactly six characters 0-9 or a-f)
def valid_hcl(passport):
    nums = [0,1,2,3,4,5,6,7,8,9]
    lets = ["a","b","c","d","e","f"]
    if "hcl" in passport.keys():
        if passport["hcl"].startswith("#") and len(passport["hcl"]) == 7:
            rest = passport["hcl"][1:]
            total_chars = 0
            for char in rest:
                if char in lets or int(char) in nums:
                    total_chars += 1
        
            if total_chars == len(rest):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

#   Define a function to check the passport has ecl, and ecl is valid (exactly one of "amb" "blu" "brn" "gry" "grn" "hzl" "oth")
def valid_ecl(passport):
    cols = ["amb","blu","brn","gry","grn","hzl","oth"]
    if "ecl" in passport.keys():
        if passport["ecl"] in cols:
            return True
        else:
            return False
    else:
        return False

#   Define a function to check the passport has a pid, and the pid is valid (a 9 digit number including leading zeroes)
def valid_pid(passport):
    nums = [0,1,2,3,4,5,6,7,8,9]
    if "pid" in passport.keys():
        if (len(passport["pid"]) == 9):
            total = 0
            for char in passport["pid"]:
                if int(char) in nums:
                    total +=1
            if total == 9:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


#   Define the function that checks all of the necessary traits
def valid(passport):
    if valid_byr(passport) and valid_iyr(passport) and valid_eyr(passport) and valid_hgt(passport) and valid_hcl(passport) and valid_ecl(passport) and valid_pid(passport):
        return True
    else:
        return False


#   Find and store the number of valid passports in passports

valid_passports = 0

for passport in passports:
    if valid(passport):
        valid_passports += 1

print("The solution to Part Two is", valid_passports)

    

    


        