from collections import defaultdict
from math import floor

# Import and filter data.
with open("./data/day_five_input.txt") as file:
    data = file.readlines()

rules = [(row[0:2], row[3:5]) for row in data if "|" in row]
updates = [row for row in data if "|" not in row and row != "\n"]

# Process rules.
processed_rules = defaultdict(list)
for rule in rules:
    processed_rules[int(rule[0])].append(int(rule[1]))


def find_middle_numbers(updates):
    # Find middle numbers
    answer = 0
    for update in updates:
        if len(update) % 2 == 0:
            answer += int(update[int(len(update) / 2)])
        else:
            answer += int(update[floor(len(update) / 2)])
    return answer


def find_updates(updates, correct_flag=True):
    relevant_updates = []
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
        if correct_flag:
            if update_count == update_length:
                relevant_updates.append(update)
        elif update_count != update_length:
            relevant_updates.append(update)
    return relevant_updates


# Part 1
correct_updates = find_updates(updates)
# print(find_middle_numbers(correct_updates))

# Part 2
incorrect_updates = find_updates(updates, False)

ordered_updates = []
for update in incorrect_updates:
    for index, number in enumerate(update):
        to_avoid = processed_rules.get(number)
        to_avoid_indexes = []
        if to_avoid:
            for n in to_avoid:
                try:
                    to_avoid_indexes.append(update.index(n))
                except:
                    pass

print(find_middle_numbers(ordered_updates))
