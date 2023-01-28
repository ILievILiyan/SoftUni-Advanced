text = input()
set_with_chars = set()

for ch in text:
    set_with_chars.add(ch)

for ch in sorted(set_with_chars):
    print(f'{ch}: {text.count(ch)} time/s')