import sys
from io import StringIO
from itertools import product


# test case 1
input_sample_a = "1 2"
input_sample_b = "3 4"


original_stdin = sys.stdin
sys.stdin = StringIO(input_sample_a)

a = [int(x) for x in input().split()]
sys.stdin = StringIO(input_sample_b)
b = [int(x) for x in input().split()]
list_prod = list(product(a,b))
# print(list_prod)
str_to_print = ""
for x in list_prod:
    str_to_print += str(x) + " "
# print(a)
# print(b)
print(str_to_print.strip())