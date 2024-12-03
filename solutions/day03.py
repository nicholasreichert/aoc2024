import re

with open('input/day03.txt', 'r') as file:
    data = file.read()
total1 = 0
total2 = 0
enabled = True
pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
matches = re.findall(pattern, data)

for match in matches:
    a = match[0]
    b = match[1]
    do = match[2]
    dont = match[3]

    if do or dont:
        if do:
            enabled = True
        elif dont:
            enabled = False
    else:
        if a and b:
            x = int(a) * int(b)
            total1 += x
            if enabled == True:
                total2 += x

print(total1, total2)