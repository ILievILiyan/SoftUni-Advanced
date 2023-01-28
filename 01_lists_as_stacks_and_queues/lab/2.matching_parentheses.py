text = input()
indexes = []

for i in range(len(text)):
    if text[i] == "(":
        indexes.append(i)
    elif text[i] == ")":
        start_i = indexes.pop()
        print(f'{text[start_i:i+1]}')

