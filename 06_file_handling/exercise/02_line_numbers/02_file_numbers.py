output_text = []
try:
    with open("text.txt", "r") as file:
        text = file.readlines()
except FileNotFoundError:
    print("File not found.")

with open("output_file.txt", "w") as file:
    for row in range(len(text)):
        count_letters = 0
        count_marks = 0

        for letter in text[row]:
            if letter.isalpha():
                count_letters += 1
            elif not letter.isalnum() and not letter.isspace() and not letter.isdigit():
                count_marks += 1

        file.write(f'Line {row + 1}: {text[row][:-1]} ({count_letters}) ({count_marks})\n')
