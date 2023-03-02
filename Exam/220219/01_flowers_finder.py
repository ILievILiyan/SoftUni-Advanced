from collections import deque

vowels = deque(x for x in input().split())
consonants = deque(x for x in input().split())

words = deque(["rose", "tulip", "lotus", "daffodil"])
words_copy = words.copy()
len_words = len(words)
index_of_found_word = 0

found_word = False
while vowels and consonants and not found_word:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for i in range(len_words):
        current_word = words[i]

        while vowel in current_word:
            current_word = current_word.replace(vowel, "")
        while consonant in current_word:
            current_word = current_word.replace(consonant, "")
        words[i] = current_word

        if len(current_word) == 0:
            found_word = True
            index_of_found_word = i
            break

if found_word:
    print(f'Word found: {words_copy[index_of_found_word]}')
else:
    print("Cannot find any word!")

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')
