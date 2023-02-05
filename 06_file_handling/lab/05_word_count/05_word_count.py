import re


def read_searched_words():
    searched_words = []
    try:
        with open("words.txt", "r") as file:
            searched_words = file.read().split()
        return searched_words
    except FileNotFoundError:
        print("File words.txt for searched words not found")


def calculate_words_count(searched_words):
    words_dict = {}
    try:
        with open("input.txt", "r") as file:
            text = file.read()
            for word in searched_words:
                pattern = fr"\b{word}\b"
                count = len(re.findall(pattern, text, re.IGNORECASE))
                words_dict[word] = count
        return words_dict
    except FileNotFoundError:
        print("File input.txt for text not found")


def output_calculations(result):
    with open("output.txt", "w") as file:
        sorted_dict = sorted(result.items(), key=lambda x: -x[1])
        for key, value in sorted_dict:
            file.write(f'{key} - {value}\n')


words = read_searched_words()
dict_count = calculate_words_count(words) if words else None
output_calculations(dict_count) if dict_count else None
