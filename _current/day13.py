# # testing example
# earliest = 939
# ids = [7, 13, 59, 31, 19]

with open("day13input.txt", "r") as file:
    data = file.read().split("\n")
    earliest = int(data[0])
    ids = data[1].split(",")
    ids = [int(id) for id in ids if id != "x"]


waittimes = []
for id in ids:
    mod = earliest % id
    if mod == 0:
        waittimes.append( (id, mod) )
    else:
        waittimes.append( (id, id - mod) )

min = [10000000000000, 100000000000]

for waittime in waittimes:
    if waittime[1] < min[1]:
        min = list(waittime)

print("The solution to Part One is", min[0] * min[1])

#   Part Two

from math import gcd

def mod_inv(a, mod):
    ''' Find x such that ax == 1 % mod. '''
    ans = 0
    for x in range(0, mod):
        if a*x % mod == 1:
            ans = x

    return ans

#   Need to parse the data differently
with open("day13input.txt", "r") as file:
    data = file.read().split("\n")
    schedule = list(data[1].split(","))

#   Get the product of all bus ids
N = 1
for id in schedule:
    if id != "x":
        N *= int(id)

#   solves the mod system
def mod_solve():
    solution = 0
    for id in schedule:
        if id != "x":
            k = int(id)
            i = schedule.index(id) % k # 'offset from t'
            a = (k - i) % k
            
            n = N // k # product of all but 1
            m = mod_inv(n, k)

            solution += a*n*m
        
    return solution % N


print("The solution to Part Two is", mod_solve())
