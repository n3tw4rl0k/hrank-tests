from io import StringIO
import sys

# test case 1
input_sample = """2 2
1 2
3 4"""
sys.stdin = StringIO(input_sample)

import numpy

nm_list = input().split()

n = int(nm_list[0])
m = int(nm_list[1])

n_list = []

for _ in range(n):
    n_list.append([int(x) for x in input().split()])

my_array = numpy.array(n_list)
my_array_s = numpy.sum(my_array, axis = 0)
my_array_p = numpy.prod(my_array_s, axis = 0)

print(my_array_p)