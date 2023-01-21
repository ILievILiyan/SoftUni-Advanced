from collections import deque

expression = deque(x for x in input().split())
current_numbers = deque()
final_num = None

operations_func = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

while expression:
    current_num = expression.popleft()
    if current_num not in operations_func:
        current_numbers.append(int(current_num))
    else:
        operator = current_num
        final_num = 0

        while len(current_numbers) > 1:
            if operator == "*" or operator == "/":
                final_num = 1

            num1 = current_numbers.popleft()
            num2 = current_numbers.popleft()
            final_num = int(operations_func[operator](num1, num2))
            current_numbers.appendleft(final_num)

        expression.appendleft(str(final_num))
        current_numbers.clear()

print(final_num)
