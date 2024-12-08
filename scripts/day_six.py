from collections import namedtuple
from copy import copy

Position = namedtuple("Position", ["coordinate", "direction"])

# Import and filter data.
with open("./data/day_six_input.txt") as file:
    data = file.readlines()

ROW_LENGTH = 12  # 143


# Functions.
def find_starting_position(coordinates):
    start = [(key, value) for key, value in coordinates.items() if value == "^"][0]
    starting_position = Position(start[0], start[1])
    return starting_position


def add_border(data):
    horizontal_border = ["!" for n in range(0, ROW_LENGTH)]
    horizontal_border.append("\n")
    new_data = [horizontal_border]
    for line in data:
        new_line = [character for character in line if character != "\n"]
        new_line.insert(0, "!")
        new_line.append("!\n")
        new_data.append(new_line)
    horizontal_border = ["!" for n in range(0, ROW_LENGTH)]
    horizontal_border.append("\n")
    new_data.append(horizontal_border)
    maze = ""
    for line in new_data:
        maze += "".join(line)
    return maze


def create_coordinates(maze):
    maze = [position for position in maze if position != "\n"]
    coordinates = {}
    for index, position in enumerate(maze):
        coordinates[index] = position
    return coordinates


def count_unique_positions(position, coordinates):
    direction_length = {"^": ROW_LENGTH, ">": -1, "<": 1, "v": -ROW_LENGTH}
    positions_crossed = []

    while not None:
        if position.direction in ("^", "v"):
            length_to_walk = direction_length[position.direction]
            next_position = position.coordinate - length_to_walk
            if coordinates[next_position] == "!":
                break
            elif coordinates[next_position] not in ("#"):
                position = Position(
                    position.coordinate - length_to_walk, position.direction
                )
            else:
                if position.direction == "^":
                    position = Position(position.coordinate, ">")
                else:
                    position = Position(position.coordinate, "<")
        if position.direction in ("<", ">"):
            length_to_walk = direction_length[position.direction]
            next_position = position.coordinate - length_to_walk
            if coordinates[next_position] == "!":
                break
            if coordinates[next_position] not in ("#"):
                positions_crossed.append(next_position)
                position = Position(
                    position.coordinate - length_to_walk, position.direction
                )
            else:
                if position.direction == ">":
                    position = Position(position.coordinate, "v")
                else:
                    position = Position(position.coordinate, "^")

    return len(set(positions_crossed))


# Part 1.
# maze = add_border(data)
# coordinates = create_coordinates(maze)
# start = find_starting_position(coordinates)
# print(count_unique_positions(start, coordinates))

# Part 2.


def count_unique_positions_v2(position, coordinates):

    maze_length = len([character for character in maze if character not in ("!", "\n")])
    direction_length = {"^": ROW_LENGTH, ">": -1, "<": 1, "v": -ROW_LENGTH}

    count = 0
    while not None:
        count += 1
        if count > maze_length:
            return 1
        if position.direction in ("^", "v"):
            length_to_walk = direction_length[position.direction]
            next_position = position.coordinate - length_to_walk
            if coordinates[next_position] == "!":
                return 0
            elif coordinates[next_position] not in ("#", "X"):
                position = Position(
                    position.coordinate - length_to_walk, position.direction
                )
            else:
                if position.direction == "^":
                    position = Position(position.coordinate, ">")
                else:
                    position = Position(position.coordinate, "<")
        if position.direction in ("<", ">"):
            length_to_walk = direction_length[position.direction]
            next_position = position.coordinate - length_to_walk
            if coordinates[next_position] == "!":
                return 0
            if coordinates[next_position] not in ("#", "X"):
                position = Position(
                    position.coordinate - length_to_walk, position.direction
                )
            else:
                if position.direction == ">":
                    position = Position(position.coordinate, "v")
                else:
                    position = Position(position.coordinate, "^")


maze = add_border(data)
coordinates = create_coordinates(maze)
start = find_starting_position(coordinates)

permutations = []
for index, character in enumerate(coordinates.values()):
    maze_copy = copy(maze)
    new_coordinates = create_coordinates(maze_copy)
    if coordinates[index] not in ("!", "^", "#"):
        new_coordinates[index] = "X"
        permutations.append(new_coordinates)

count = 0
for i, p in enumerate(permutations):
    count += count_unique_positions_v2(start, p)

print(count)
