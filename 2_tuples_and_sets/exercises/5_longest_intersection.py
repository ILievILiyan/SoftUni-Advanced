num_of_lines = int(input())
first_set = set()
second_set = set()
longest_intersection = set()

for _ in range(num_of_lines):
    first_pair, second_pair = [x.split(",") for x in input().split("-")]
    start_first_pair = int(first_pair[0])
    end_first_pair = int(first_pair[1])
    start_second_pair = int(second_pair[0])
    end_second_pair = int(second_pair[1])

    for digit in range(start_first_pair, end_first_pair+1):
        first_set.add(digit)

    for digit in range(start_second_pair, end_second_pair+1):
        second_set.add(digit)
    if len(first_set.intersection(second_set)) > len(longest_intersection):
        longest_intersection = first_set.intersection(second_set)
    first_set.clear()
    second_set.clear()

print(f'Longest intersection is [{", ".join(map(str, longest_intersection))}] with length {len(longest_intersection)}')