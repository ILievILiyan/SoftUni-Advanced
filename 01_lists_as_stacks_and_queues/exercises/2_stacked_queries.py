num = int(input())
my_list = []
new_list = []

for _ in range(num):
    command = input().split(" ")
    cmd = command[0]
    if cmd == "1":
        my_list.append(int(command[1]))
    elif len(my_list) > 0:
        if cmd == "2":
            my_list.pop()
        elif cmd == "3":
            print(max(my_list))
        elif cmd == "4":
            print(min(my_list))

while my_list:
    new_list.append(str(my_list.pop()))

print(", ".join(new_list))
