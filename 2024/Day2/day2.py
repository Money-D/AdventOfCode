reports = []


def parse_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        nums = line.split()
        reports.append(nums)


def is_safe(report):
    increasing = int(report[0]) < int(report[-1])

    prev = int(report[0])
    dampener = 1
    for level in report[1:]:
        level = int(level)
        if increasing and (level > prev + 3 or level <= prev):
            return False
        elif not increasing and (level >= prev or level < prev - 3):
            return False

        prev = level

    return True


def count_safe_reports():
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
    return count


if __name__ == '__main__':
    parse_input_file('input.txt')

    safe_reports = count_safe_reports()
    print('Safe reports:' + safe_reports)
    p
