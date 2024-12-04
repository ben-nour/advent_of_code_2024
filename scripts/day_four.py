import copy

with open("./data/day_four_input.txt") as file:
    data = file.readlines()

# Adding . padding to left and right column.
cleaned_lines = []
for line in data:
    cleaned_line = ["."]
    for letter in line:
        if letter != "\n":
            cleaned_line.append(letter)
    cleaned_line.insert(len(cleaned_line), ".")
    cleaned_line.insert(len(cleaned_line), "\n")
    cleaned_lines.append(cleaned_line)

first_list = cleaned_lines[0]
for cleaned_line in cleaned_lines[1:]:
    first_list.extend(cleaned_line)

# Create grid to visualise padding.
grid = ""
for letter in first_list:
    grid += letter
print(grid)

# Coordinates
coordinates = {}
for index, letter in enumerate(first_list):
    coordinates.update({index: letter})


xmas_count = 0
for index, letter in enumerate(first_list):
    surrounding_coordinates = []
    line_jump = 143
    if letter == "X":
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
            coordinates.get(index + line_jump) == "M"
            and coordinates.get(index + (line_jump * 2)) == "A"
            and coordinates.get(index + (line_jump * 3)) == "S"
        ):
            xmas_count += 1

        # Above
        if (
            coordinates.get(index - line_jump) == "M"
            and coordinates.get(index - (line_jump * 2)) == "A"
            and coordinates.get(index - (line_jump * 3)) == "S"
        ):
            xmas_count += 1

        # Bottom right
        if (
            coordinates.get(index + line_jump + 1) == "M"
            and coordinates.get(index + (line_jump * 2) + 2) == "A"
            and coordinates.get(index + (line_jump * 3) + 3) == "S"
        ):
            xmas_count += 1

        # Bottom left.
        if (
            coordinates.get(index + line_jump - 1) == "M"
            and coordinates.get(index + (line_jump * 2) - 2) == "A"
            and coordinates.get(index + (line_jump * 3) - 3) == "S"
        ):
            xmas_count += 1

        # Top left
        if (
            coordinates.get((index - line_jump) - 1) == "M"
            and coordinates.get(index - (line_jump * 2) - 2) == "A"
            and coordinates.get(index - (line_jump * 3) - 3) == "S"
        ):
            xmas_count += 1

        # Top right
        if (
            coordinates.get((index - line_jump) + 1) == "M"
            and coordinates.get(index - (line_jump * 2) + 2) == "A"
            and coordinates.get(index - (line_jump * 3) + 3) == "S"
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
14 ?
top_right = 4
17 ?

"""
