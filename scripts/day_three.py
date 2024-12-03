import math
import re

with open("./data/day_three_input.txt") as file:
    data = file.read()

# Part 1
regex = r"mul\([0-9]+,*[0-9]+\)"
matches = re.findall(regex, data)
numbers = 0
for match in matches:
    for to_replace in ("mul", "(", ")"):
        match = match.replace(to_replace, "")
    match_numbers = [int(element) for element in match.split(",")]
    numbers += math.prod(match_numbers)
print(numbers)
