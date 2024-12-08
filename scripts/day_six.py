from collections import namedtuple

Position = namedtuple("Position", ["coordinate", "direction"])

# Import and filter data.
with open("./data/day_six_input.txt") as file:
    data = file.read()


def create_coordinates(maze):
    maze = [position for position in data if position != "\n"]
    coordinates = {}
    for index, position in enumerate(maze):
        coordinates[index] = position
    return coordinates


def count_positions(coordinates):
    start = [(key, value) for key, value in coordinates.items() if value == "^"][0]
    starting_position = Position(start[0], start[1])
    return starting_position


def move(position, coordinates):
    direction_length = {"^": 12, ">": -1, "<": 1, "v": -12}
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


coordinates = create_coordinates(data)
print(coordinates)
start = count_positions(coordinates)
foo = move(start, coordinates)
print(foo)
