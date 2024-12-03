def is_safe_report(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]

    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return all_increasing or all_decreasing


def is_safe_with_dampener(report):
    if is_safe_report(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True
    return False


with open("day2.txt", "r") as file:
    reports = [[int(num) for num in line.split()] for line in file]

part2 = sum(is_safe_with_dampener(report) for report in reports)
part1 = sum(is_safe_report(report) for report in reports)

print("Total number of safe reports:", part1)

print("Total number of safe reports (with Dampener):", part2)