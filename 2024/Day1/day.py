from typing import Counter


list1 = []
list2 = []


def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        nums = line.split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))


def calculate_diff():
    list1.sort()
    list2.sort()

    diff = 0
    for num1, num2 in zip(list1, list2):
        diff += abs(num1 - num2)

    return diff


def similarity_score():
    list2_freq = Counter(list2)

    similarity_score = 0
    for num in list1:
        if num in list2_freq:
            similarity_score += num * list2_freq[num]

    return similarity_score


if __name__ == '__main__':
    parse_input('input.txt')

    list1.sort()
    list2.sort()

    diff = calculate_diff()
    similarity_score = similarity_score()

    print(diff)
    print(similarity_score)
