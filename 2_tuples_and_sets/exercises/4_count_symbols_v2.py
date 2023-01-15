text = input()
chars_dict = dict()

for ch in text:
    if ch not in chars_dict.keys():
        chars_dict[ch] = 0
    chars_dict[ch] += 1

sorted_chars = sorted(chars_dict.items(), key=lambda x: x)

for k,v in sorted_chars:
    print(f'{k}: {v} time/s')
