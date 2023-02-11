symbols_to_change = ["-", ",", ".", "!", "?"]

try:
    with open("text.txt", "r") as file:
        text = file.readlines()

    for i in range(0, len(text), 2):
        for current_symbol in symbols_to_change:
            text[i] = text[i].replace(current_symbol, "@")

        list_text = text[i].split()
        reversed_text = reversed(list_text)
        print(" ".join(reversed_text))
        # print(*text[i].split()[::-1], sep=" ")

except FileNotFoundError:
    print("File not found.")
