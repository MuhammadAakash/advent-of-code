from collections import Counter


with open("day1.txt", "r") as file:
    pairs = [list(map(int, line.split())) for line in file]

left_list = [pair[0] for pair in pairs]
right_list = [pair[1] for pair in pairs]

left_list.sort()
right_list.sort()

right_counter = Counter(right_list)

total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
similar_score = sum(left * right_counter.get(left, 0) for left in left_list)

print('Total distance is :', total_distance)
print('Similar score is :', similar_score)