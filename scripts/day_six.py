from collections import namedtuple

Position = namedtuple("Position", ["coordinate", "direction"])

# Import and filter data.
with open("./data/day_six_input.txt") as file:
    data = file.readlines()


# Functions.
def find_starting_position(coordinates):
    start = [(key, value) for key, value in coordinates.items() if value == "^"][0]
    starting_position = Position(start[0], start[1])
    return starting_position


def add_border(data):
    horizontal_border = ["!" for n in range(0, 132)]
    horizontal_border.append("\n")
    new_data = [horizontal_border]
    for line in data:
        new_line = [character for character in line if character != "\n"]
        new_line.insert(0, "!")
        new_line.append("!\n")
        new_data.append(new_line)
    horizontal_border = ["!" for n in range(0, 132)]
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
    direction_length = {"^": 132, ">": -1, "<": 1, "v": -132}
    positions_crossed = []

    while not None:
        if position.direction in ("^", "v"):
            length_to_walk = direction_length[position.direction]
            next_position = position.coordinate - length_to_walk
            if coordinates[next_position] == "!":
                break
            elif coordinates[next_position] != "#":
                positions_crossed.append(next_position)
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
            if coordinates[next_position] != "#":
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
maze = add_border(data)
coordinates = create_coordinates(maze)
start = find_starting_position(coordinates)
print(count_unique_positions(start, coordinates))
