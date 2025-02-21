import sys
from io import StringIO

orig_stdin = sys.stdin

# test case 1
input_sample = """2
hacker book"""

# test case 2
# input_sample = """3
# programming is awesome"""

sys.stdin = StringIO(input_sample)

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            # this was the problem ++score, this was bogus syntax, this does not exist in python.
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))