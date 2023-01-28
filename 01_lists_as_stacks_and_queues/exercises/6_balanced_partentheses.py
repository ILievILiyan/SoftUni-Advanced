from collections import deque

text = deque(input())
open_parentheses = deque()

while text:
    left_parentheses = text.popleft()
    if left_parentheses in "([{":
        open_parentheses.append(left_parentheses)

    elif not open_parentheses:
        print("NO")
        break
    else:
        if f"{open_parentheses.pop() + left_parentheses}" not in "{}()[]":
            print("NO")
            break
else:
    print("YES")