import re


def read_searched_words():
    searched_words = []
    with open("words.txt", "r") as file:
        searched_words = file.read().split()
    return searched_words


def calculate_words_count(searched_words):
    words_dict = {}
    with open("input.txt", "r") as file:
        text = file.read()
        for word in searched_words:
            pattern = fr"\b{word}\b"
            count = len(re.findall(pattern, text, re.IGNORECASE))
            words_dict[word] = count
    return words_dict


def output_calculations(result):
    with open("output.txt", "w") as file:
        sorted_dict = sorted(result.items(), key=lambda x: -x[1])
        for key, value in sorted_dict:
            file.write(f'{key} - {value}\n')


words = read_searched_words()
dict_count = calculate_words_count(words)
output_calculations(dict_count)