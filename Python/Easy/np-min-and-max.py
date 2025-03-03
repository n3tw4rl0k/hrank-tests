from io import StringIO
import sys

# test case 1
input_sample = """4 2
2 5
3 7
1 3
4 0"""

sys.stdin = StringIO(input_sample)

import numpy

nm_list = input().split()

n = int(nm_list[0])
m = int(nm_list[1])

n_list = []

for _ in range(n):
    n_list.append([int(x) for x in input().split()])

# print(n_list)
my_array = numpy.array(n_list)
# print(my_array)
my_array_min = numpy.min(my_array, axis = 1)
# print(my_array_min)
my_array_max = numpy.max(my_array_min)
print(my_array_max)
