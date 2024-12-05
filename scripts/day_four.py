import copy

with open("./data/day_four_input.txt") as file:
    data = file.readlines()


def pad_grid(data):
    """
    Pad grids with . characters
    to prevent out-of-bound problems.
    """
    padded_rows = []
    for row in data:
        padded_row = ["."]
        for letter in row:
            if letter != "\n":
                padded_row.append(letter)
        padded_row.insert(len(padded_row), ".")
        padded_row.insert(len(padded_row), "\n")
        padded_rows.append(padded_row)
    return padded_rows


def create_coordinates(grid):
    # Create string.
    grid_string = padded_grid[0]
    for padded_row in padded_grid[1:]:
        grid_string.extend(padded_row)

    # Create coordinates.
    coordinates = {}
    for index, letter in enumerate(grid_string):
        coordinates.update({index: letter})
    return grid_string, coordinates


padded_grid = pad_grid(data)
grid_string, coordinates = create_coordinates(padded_grid)

# Part 1.
xmas_count = 0
for index, letter in enumerate(grid_string):
    line_jump = 143  # 143
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
