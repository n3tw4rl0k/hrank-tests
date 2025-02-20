import sys
from io import StringIO

orig_stdin = sys.stdin

# test case 1
input_sample = """4
bcdef
abcdefg
bcde
bcdef"""

sys.stdin = StringIO(input_sample)

n_words = int(input())

words_dict = {}

for i in range(n_words):
    word_to_add = input()
    if word_to_add not in words_dict.keys():
        words_dict[word_to_add] = 1
    else:
        words_dict[word_to_add] += 1

print(len(words_dict.keys()))
for v in words_dict.values():
    print(v, end=" ")
