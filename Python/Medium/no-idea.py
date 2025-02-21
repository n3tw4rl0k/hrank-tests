import sys
from io import StringIO

orig_stdin = sys.stdin

# test case 1
input_sample = """3 2
1 5 3
3 1
5 7"""

sys.stdin = StringIO(input_sample)

n_int_range, set_len = map(int, input().split())
# print(n_int_range)  # we could use for extra checking the len correctness, but not really needed
# print(set_len)      # same

numbers_to_chk = list(map(int, input().split()))

# we need to use sets , they are faster for search, instead of list like
# a_set = [int(z) for z in input().split()]
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

happiness_level = 0

for x in numbers_to_chk:
    if x in a_set:
        happiness_level += 1
    if x in b_set:
        happiness_level -= 1

print(happiness_level)

sys.stdin = orig_stdin