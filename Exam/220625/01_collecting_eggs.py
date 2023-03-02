from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
pieces_of_paper = deque([int(x) for x in input().split(", ")])
eggs_box = 0
MIN_SIZE_OF_EGGS_BOX = 50

while eggs and pieces_of_paper:
    egg = eggs.popleft()

    if egg <= 0:
        continue
    if egg == 13:
        pieces_of_paper[0], pieces_of_paper[-1] = pieces_of_paper[-1], pieces_of_paper[0]
        continue

    paper = pieces_of_paper.pop()
    total_size = egg + paper

    if total_size <= MIN_SIZE_OF_EGGS_BOX:
        eggs_box += 1

if eggs_box:
    print(f'Great! You filled {eggs_box} boxes.')
else:
    print('Sorry! You couldn\'t fill any boxes!')

if eggs:
    print(f'Eggs left: {", ".join(str(x) for x in eggs)}')
elif pieces_of_paper:
    print(f'Pieces of paper left: {", ".join(str(x) for x in pieces_of_paper)}')
