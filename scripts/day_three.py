import math
import re

with open("./data/day_three_input.txt") as file:
    data = file.read()

# Part 1
regex = r"mul\(\d+,*\d+\)"
matches = re.findall(regex, data)
answer = 0
for match in matches:
    for to_replace in ("mul", "(", ")"):
        match = match.replace(to_replace, "")
    match_numbers = [int(element) for element in match.split(",")]
    answer += math.prod(match_numbers)

print(f"Part 1 answer: {answer}")

# Part 2
regex = r"don't\(\)|do\(\)|mul\(\d+,*\d+\)"
matches = re.findall(regex, data)
answer = 0
flag = True
for index, match in enumerate(matches):
    if re.fullmatch(r"don't\(\)", match):
        flag = False
    if re.fullmatch(r"do\(\)", match):
        flag = True
    if re.fullmatch(r"mul\(\d+,*\d+\)", match):
        for to_replace in ("mul", "(", ")"):
            match = match.replace(to_replace, "")
        match = [int(element) for element in match.split(",")]
        match = math.prod(match)
        if flag:
            answer += match
print(f"Part 2 answer: {answer}")
