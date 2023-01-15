num_of_students = int(input())
students = {}

for _ in range(num_of_students):
    name, grade = input().split()

    if name not in students.keys():
        students[name] = []
    students[name].append(float(grade))


for name, grade in students.items():
    print(f"{name} -> {' '.join([f'{el:.2f}' for el in grade])} (avg: {sum(grade)/len(grade):.2f})")
