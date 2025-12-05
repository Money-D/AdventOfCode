import math
filename = 'day1.txt'
test_file = 'day1_test.txt'
rotations = []

with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        direction, turn = line[0], int(line[1:])
        rotations.append((direction, turn))

dial = 50
zeros = 0

for rotation in rotations:
    dir, turns = rotation
    dial_before = dial
    if dir == 'R':
        dial += turns
    elif dir == 'L':
        dial -= turns

    if dial_before == 0:
        zeros += turns // 100
    elif dial <= 0 or dial > 99:
        zeros += (dial // 100) + 1

    dial = dial % 100


print(zeros)
