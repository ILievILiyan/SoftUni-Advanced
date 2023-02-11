def words_sorting(*args):
    words_dict = {}

    for word in args:
        current_sum = 0
        for w in word:
            current_sum += ord(w)
        words_dict[word] = current_sum

    total_sum = sum(words_dict.values())
    if total_sum % 2 != 0:
        sorted_words = sorted(words_dict.items(), key=lambda x: -x[1])
    else:
        sorted_words = sorted(words_dict.items(), key=lambda x: (x[0]))

    result = ""
    for key, value in sorted_words:
        result += f"{key} - {value}\n"
    return result

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print("------------------------------------")
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print("------------------------------------")
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

