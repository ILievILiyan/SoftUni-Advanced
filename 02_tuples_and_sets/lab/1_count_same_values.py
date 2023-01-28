numbers = (float(x) for x in input().split())
num_dict = {}

for num in numbers:
    if num not in num_dict.keys():
        num_dict[num] = 0
    num_dict[num] += 1

for number, repetition in num_dict.items():
    print(f"{number} - {repetition} times")