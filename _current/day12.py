#   Load in example input
with open("day12example.txt", "r") as file:
    example = file.read().split("\n")

#   Load in puzzle input
with open("day12input.txt", "r") as file:
    instructions = file.read().split("\n")

#   Part 1 functions
def move(current_east, current_north, instruct):
    '''Takes the ships current position east, north and applies the instruction given as a single character N, S, E, W followed by a number to change the position of the ship. Outputs a tuple new_east, new_north. '''

    compass = instruct[:1] # N, E, S, W
    change = int(instruct[1:])

    east = current_east
    north = current_north

    if compass == "N":
        north += change
    elif compass == "S":
        north -= change
    elif compass == "E":
        east += change
    elif compass == "W":
        east -= change

    return east, north


def turn(current_direction, instruct):
    '''Takes the ships current direction N, E, S, W and applies the instruction givn as a single character R or L and a number (90, 180, 270) to change the direction of the ship. Outputs the new direction  '''

    translation = {"N" : 0, "E" : 1, "S" : 2, "W" : 3}
    rev_translation = {0 : "N", 1 : "E", 2 : "S", 3 : "W"}

    direction = translation[current_direction]

    cmd = instruct[:1]
    change = int(instruct[1:]) // 90  # so change is 1, 2, or 3 and we can work mod 4

    if cmd == "R":
        direction += change
    elif cmd == "L":
        direction -= change

    direction = direction % 4

    direction_letter = rev_translation[direction]
    return direction_letter


def forward(current_east, current_north, current_direction, instruct):
    ''' Takes the ships current position and direction, and applies the instruction given by a single character F and a number to change the position of the ship based on moving forward. Outputs the new position (direction unchanged).'''
    east = current_east
    north = current_north

    directed_instruct = instruct.replace("F", current_direction)

    east, north = move(east, north, directed_instruct)

    return east, north


# represent north/south and east/west as north and east and use negation for south and west
# ship starts at (east, north) = (0, 0)
east = 0
north = 0

#   Start facing east
dir = "E"

for instruction in instructions:
    if instruction.startswith("F"):
        east, north = forward(east, north, dir, instruction)
    elif instruction.startswith(("R", "L")):
        dir = turn(dir, instruction)
    elif instruction.startswith(("N", "E", "S", "W")):
        east, north = move(east, north, instruction)


manhatten = abs(east) + abs(north)

print("The solution to Part One is", manhatten) # Solution is 1177!

#   Part two    #


#   forward and turn now do very different things, but move still works - it now moves the waypoint instead of the ship - the waypoint doesnt cause the ship to move, but the waypoint moves when the ship changes
#   We no longer care where the ship is facing, as forward means to move to the waypoint a certain number of times
def move_waypoint(waypoint_east, waypoint_north, instruct):
    '''Takes the waypoints current position east, north and applies the instruction given as a single character N, S, E, W followed by a number to change the position of the waypoint. Outputs a tuple new_east, new_north. '''

    compass = instruct[:1] # N, E, S, W
    change = int(instruct[1:])

    east = waypoint_east
    north = waypoint_north

    if compass == "N":
        north += change
    elif compass == "S":
        north -= change
    elif compass == "E":
        east += change
    elif compass == "W":
        east -= change

    return east, north


def forward_waypoint(ship_east, ship_north, waypoint_east, waypoint_north, instruct):
    ''' Takes the ships position and the waypoints position and changes the ships position by the amount in the instruction x the waypoints position'''
    scalar = int(instruct[1:])

    east = ship_east + scalar * waypoint_east
    north = ship_north + scalar * waypoint_north
    
    return east, north

def rotate_waypoint(waypoint_east, waypoint_north, instruct):
    ''' rotates the waypoint relative to the ship, so that (east, north) becomes (+- east, +- north) depending on the amount of rotation required.'''
    
    rotation = int(instruct[1:])
    orientation = instruct[0]
    east = waypoint_east
    north = waypoint_north

    if orientation == "R": # clockwise
        if rotation == 90:
            east, north = north, -1*east
        elif rotation == 180:
            east, north = -1*east, -1*north
        elif rotation == 270:
            east, north = -1*north, east
    elif orientation == "L": # countclockwise
        if rotation == 90:
            east, north = -1*north, east
        elif rotation == 180:
            east, north = -1*east, -1*north
        elif rotation == 270:
            east, north = north, -1*east


    return east, north

ship_east = 0
ship_north = 0

#   Waypoint starts 10 units east, 1 unit north and is always relative to ship's position
waypoint_east = ship_east + 10
waypoint_north = ship_north + 1

#   Run through the instructions
for instruction in instructions:
    if instruction.startswith("F"):
        ship_east, ship_north = forward_waypoint(ship_east, ship_north, waypoint_east, waypoint_north, instruction)
    elif instruction.startswith(("R", "L")):
        waypoint_east, waypoint_north = rotate_waypoint(waypoint_east, waypoint_north, instruction)
    elif instruction.startswith(("N", "S", "E", "W")):
        waypoint_east, waypoint_north = move_waypoint(waypoint_east, waypoint_north, instruction)

#   Compute and return the Manhatten distance
manhatten = abs(ship_east) + abs(ship_north)

print("The solution to Part Two is", manhatten)

# print("ship: ", ship_east, ship_north, "waypoint: ", waypoint_east, waypoint_north)