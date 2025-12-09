

with open("day2_input.txt") as f:
    content = f.read()
    string_pairs = [r.split('-') for r in content.split(',')]
    ranges = [[int(l), int(r)] for l, r in string_pairs]


def isValidPart1(id: int):
    # if num has odd length it is not valid
    id = str(id)
    if len(id) % 2 == 1:
        return True
    left = id[:len(id)//2]
    right = id[len(id)//2:]
    if left == right:
        return False

    return True


def isInvalidPart2(id: int):
    id = str(id)

    for jump in range(1, len(id)//2+1):
        if len(id) % jump != 0:
            continue

        count = 0

        for start in range(0, jump):
            prev = id[start]
            for curr in range(start, len(id), jump):
                if id[curr] != prev:
                    break
                else:
                    count += 1

        if count == len(id):
            return True

    return False


def find_invalid_ids(ranges):
    invalid_ids = []
    # process each range [start, end]
    for start, end in ranges:
        # check each number in this range from start to end
        for id in range(start, end+1):
            if isInvalidPart2(id):
                invalid_ids.append(id)

    return sum(invalid_ids)


invalid_ids_sum = find_invalid_ids(ranges)
print(invalid_ids_sum)
