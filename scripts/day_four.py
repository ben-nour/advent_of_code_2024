import copy

with open("./data/day_four_input.txt") as file:
    data = [line for line in file.read() if line != "\n"]


def create_surrounding_grid(letters):
    grid = ""
    counter = 0
    for letter in letters:
        if counter == 11:
            grid += letter
            grid += "\n"
            counter = 0
            continue
        grid += letter
        counter += 1
    return grid


# Add padding columns.
# Left column
counter = 0
for fake_column in range(0, 19601, 10):
    fake_column = fake_column + counter
    counter += 1
    data.insert(fake_column, ".")

# Right
counter = 0
for fake_column in range(11, 19601, 10):
    fake_column = fake_column + counter
    counter += 2
    data.insert(fake_column, ".")


# Visualise:
print(create_surrounding_grid(data))

# Coordinates
coordinates = {}
for index, letter in enumerate(data):
    coordinates.update({index: letter})
print(coordinates)


def check_coordinates(index, coordinates, direction=None):
    letters = "MAS"
    right = index + 1
    left = index - 1
    below = index + 10
    above = index - 10
    above_left = index - 11
    above_right = index - 9
    below_right = index + 11
    below_left = index + 9
    if direction is None:
        for to_check in (
            right,
            left,
            below,
            above_left,
            above_right,
            below_right,
            below_left,
        ):
            possible_matches = []
            if (match := coordinates.get(to_check)) == "M":
                possible_matches.append(match)
            for match in possible_matches:
                check_coordinates


xmas_count = 0
for index, letter in enumerate(data):
    surrounding_coordinates = []
    if letter == "X":

        # test = check_coordinates(index, coordinates)
        # Right
        if (
            coordinates.get(index + 1) == "M"
            and coordinates.get(index + 2) == "A"
            and coordinates.get(index + 3) == "S"
        ):
            xmas_count += 1
        # Left
        if (
            coordinates.get(index - 1) == "M"
            and coordinates.get(index - 2) == "A"
            and coordinates.get(index - 3) == "S"
        ):
            xmas_count += 1

        # Below
        if (
            coordinates.get(index + 12) == "M"
            and coordinates.get(index + 24) == "A"
            and coordinates.get(index + 36) == "S"
        ):
            xmas_count += 1

        # Above
        if (
            coordinates.get(index - 12) == "M"
            and coordinates.get(index - 24) == "A"
            and coordinates.get(index - 36) == "S"
        ):
            xmas_count += 1

        # Bottom right
        if (
            coordinates.get(index + 13) == "M"
            and coordinates.get(index + 24) == "A"
            and coordinates.get(index + 35) == "S"
        ):
            xmas_count += 1

        # Bottom left.
        if (
            coordinates.get(index + 11) == "M"
            and coordinates.get(index + 22) == "A"
            and coordinates.get(index + 33) == "S"
        ):
            xmas_count += 1

        # Top left
        if (
            coordinates.get(index - 13) == "M"
            and coordinates.get(index - 24) == "A"
            and coordinates.get(index - 35) == "S"
        ):
            xmas_count += 1

        # Top right
        if (
            coordinates.get(index - 11) == "M"
            and coordinates.get(index - 22) == "A"
            and coordinates.get(index - 33) == "S"
        ):
            xmas_count += 1


print(xmas_count)

"""

right = 3
left = 2 
below = 1
above = 2
8

bottom_right = 1
bottom_left = 1
10

top_left = 4
14
top_right = 4
17

"""
