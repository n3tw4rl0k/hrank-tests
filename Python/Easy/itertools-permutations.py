# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from io import StringIO
from itertools import permutations


# test case 1
# input_sample = "HACK 2"
input_sample = "ABCD 3"

sys.stdin = StringIO(input_sample)


input_str = input().split()
# print(int(input_str[1]))
# print(input_str[0])

list_permutations = list(permutations(input_str[0], int(input_str[1])))
list_permutations.sort()
# print(list_permutations)
for x in list_permutations:
    print("".join(x for x in x))
