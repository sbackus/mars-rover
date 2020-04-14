MINIMUM_MOON_UNIT = 0
MAXIMUM_MOON_UNIT = 9
DIRECTIONS = ["N", "E", "S", "W"]

def mars_rover(commands):
    direction = "N"
    x = 0
    y = 0
    vector = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0)
    }
    for command in commands:
        if command == "F":
            vector_x, vector_y = vector[direction]
            x += vector_x
            y += vector_y
        x, y = warp_drive(x), warp_drive(y)
        direction = turn(direction, command)
    return f"{x}:{y}:{direction}"


def turn(current_heading, turn_signal):
    direction_index = DIRECTIONS.index(current_heading)
    if turn_signal == "R":
        direction_index += 1
    elif turn_signal == "L":
        direction_index -= 1

    return DIRECTIONS[direction_index % len(DIRECTIONS)]

def warp_drive(coord):
    if coord < MINIMUM_MOON_UNIT:
        return MAXIMUM_MOON_UNIT
    if coord > MAXIMUM_MOON_UNIT:
        return MINIMUM_MOON_UNIT
    return coord
