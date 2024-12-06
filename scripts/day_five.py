from collections import defaultdict
from math import floor

with open("./data/day_five_input.txt") as file:
    data = file.readlines()

rules = [(row[0:2], row[3:5]) for row in data if "|" in row]
updates = [row for row in data if "|" not in row and row != "\n"]

# Process rules.
processed_rules = defaultdict(list)
for rule in rules:
    processed_rules[int(rule[0])].append(int(rule[1]))


# Find correct updates.
correct_updates = []
for update in updates:
    update = update.split(",")
    update = [int(u) for u in update]
    update_length = len(update)
    update_count = 0
    for index, number in enumerate(update):
        to_avoid = processed_rules.get(number)
        to_avoid_indexes = []
        if to_avoid:
            for n in to_avoid:
                try:
                    to_avoid_indexes.append(update.index(n))
                except:
                    pass
            if all([index < n for n in to_avoid_indexes]):
                update_count += 1
        else:
            update_count += 1
    if update_count == update_length:
        correct_updates.append(update)

# Find middle numbers
answer = 0
for valid_update in correct_updates:
    if len(valid_update) % 2 == 0:
        answer += int(valid_update[int(len(valid_update) / 2)])
    else:
        answer += int(valid_update[floor(len(valid_update) / 2)])
print(answer)


"""
def create_ordering(rules):
    ordering = [rules[0][0], rules[0][1]]
    for index, rule in enumerate(rules[1:]):
        first_number = rule[0]
        second_number = rule[1]
        try:
            # First number.
            found_index = ordering.index(second_number)
            if first_number not in ordering:
                if found_index != 0:
                    ordering.insert(found_index - 1, first_number)
                else:
                    ordering.insert(0, first_number)
            else:
                same_number_index = ordering.index(first_number)
                if same_number_index >= found_index:
                    del ordering[same_number_index]
                    if found_index != 0:
                        ordering.insert(found_index - 1, first_number)
                    else:
                        ordering.insert(0, first_number)
            # Second number.
            if second_number not in ordering:
                ordering.insert(len(ordering), second_number)

        # Second number doesn't exist already in ordering.
        except:
            if first_number not in ordering:
                ordering.insert(
                    len(ordering), first_number
                )  # TODO - what if first_number doex exist?
            ordering.insert(len(ordering), second_number)
        if first_number == "37":
            print(first_number, second_number)
            print(ordering)
    return ordering


def find_correct_updates(updates, ordering):
    valid_updates = []

    # Find correct updates.
    for update in updates:
        update = update.split(",")
        update_length = len(update)
        update_count = 0
        for index, number in enumerate(update):
            if index == (update_length - 1):  # Last element in list.
                update_count += 1
                break
            current_number = number.strip()
            next_number = update[index + 1].strip()
            if ordering.index(current_number) < ordering.index(next_number):
                update_count += 1
        if update_count >= update_length:
            valid_updates.append(update)

    # Find middle number
    answer = 0
    for valid_update in valid_updates:
        if len(valid_updates) % 2 == 0:
            answer += int(valid_update[int(len(valid_update) / 2)])
        else:
            answer += int(valid_update[floor(len(valid_update) / 2)])
    return answer


ordering = create_ordering(rules)
print(ordering)
# answer = find_correct_updates(updates, ordering)
# print(answer)
"""
