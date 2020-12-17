with open("day15input.txt", "r") as file:
    game = file.read().split(",")
    game = [int(g) for g in game]

recents = {} # stores number_spoken : most_recent_turn, turn 1 is index 0 !!!
for i in range(len(game)-1) :
    recents[game[i]] = i

t = len(game)-1

while t < 2020:
    
    last_spoken = game[-1]

    if game.count(last_spoken) == 1:
        next_spoken = 0
        recents[last_spoken] = t
    else:
        k = recents[last_spoken]
        recents[last_spoken] = t
        next_spoken = t - k

    game.append(next_spoken)
    t += 1

print("The solution to Part One is", game[2019])

#   PART TWO

#   Using the same construction above takes too long, so instead of storing game as a list we use a dictionary for speed.

#   Two dictionaries is also too slow, so gonna try just one for the whole thing

#   And the while loop wont work for some reason UGH

with open("day15input.txt", "r") as file:
    data = file.read().split(",")
    data = [int(d) for d in data]


game = {}

for i in range(len(data)):
    game[data[i]] = i+1

last_spoken = 0 # 2 was said before for the first time
t = len(game) - 1

for i in range(len(game)+1, 30000000):
    if last_spoken in game.keys():
        diff = i - game[last_spoken]
        game[last_spoken] = i # update most recent turn and game simultaneously
        last_spoken = diff
    else:
        game[last_spoken] = i # add newly spoken numbers
        last_spoken = 0 # we say 0 if the prev number was spoken before

print("The solution to Part Two is", last_spoken)


    






    

