from copy import copy

with open("./data/day_two_input.txt") as file:
    levels = [line.split() for line in file]

LEVELS_COUNT = len(levels)


def create_list_versions(original: list) -> list:
    """
    Create different versions of a list. Each version has one element removed.
    """
    copies = []
    for index, number in enumerate(original):
        list_copy = copy(original)
        del list_copy[index]
        copies.append(list_copy)
    copies.insert(0, original)
    return copies


def process_level(level):
    for index, number in enumerate(level):
        number = int(number)
        previous_number = int(level[index - 1])
        if index == 1:
            if number - previous_number < 0:
                flag = 0
            else:
                flag = 1
        if index != 0:
            if number - previous_number > 3:
                return 1
            if number < previous_number and abs(number - previous_number) > 3:
                return 1
            if number == previous_number:
                return 1
            if number - previous_number < 0:
                new_flag = 0
            else:
                new_flag = 1
            if new_flag != flag:
                return 1
    return 0  # No issues.


# Part 1 answer.
invalid_levels = sum([process_level(level) for level in levels])
print(LEVELS_COUNT - invalid_levels)

# Part 2 answer.
invalid_levels = 0
for level in levels:
    different_versions = create_list_versions(level)
    versions_count = len(different_versions)
    errors = sum([process_level(version) for version in different_versions])
    if (
        errors < versions_count
    ):  # If just one version passes the level is considered safe.
        continue
    else:
        invalid_levels += 1

# Part 2 answer.
print(LEVELS_COUNT - invalid_levels)
