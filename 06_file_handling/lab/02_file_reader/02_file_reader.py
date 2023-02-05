
try:
    with open("numbers.txt", "r") as file:
        print(sum(int(line) for line in file.readlines()))
    #   result = 0
    #     for line in file.readlines():
    #         result += int(line)
    #   print(result)
except FileNotFoundError:
    print("File was not found")

