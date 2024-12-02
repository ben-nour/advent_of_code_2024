# Part 1.

first_list = []
second_list = []
with open("./data/day_one_input") as file:
    for line in file:
        line = line.split()
        first_list.append(int(line[0]))
        second_list.append(int(line[1]))

answer = sum(
    [
        abs(first_number - second_number)
        for first_number, second_number in zip(sorted(first_list), sorted(second_list))
    ]
)
print(answer)

# Part 2.
answer = sum(
    [first_number * (second_list.count(first_number)) for first_number in first_list]
)
print(answer)
