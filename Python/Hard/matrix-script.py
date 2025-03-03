from io import StringIO
import sys

# test case 1
# input_sample = """7 3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ir!"""

# test case 2
# input_sample = """2 4
# # i#
#  @#U"""

# test case 3
input_sample = """2 2
# 
 @"""

sys.stdin = StringIO(input_sample)

#!/bin/python3
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix_array = []
for el in matrix:
    second_matrix_l = list(x for x in el)
    matrix_array.append(second_matrix_l)

decoded_message = ""
for j in range(m):
    for i in range(n):
        decoded_message += matrix_array[i][j]

first_match = re.search(r'[a-zA-Z0-9]', decoded_message)
last_match = re.search(r'[a-zA-Z0-9][^a-zA-Z0-9]*$', decoded_message)

try:
    first_alnum_pos = first_match.start()
    last_alnum_pos = last_match.start()
    start_part = decoded_message[:first_alnum_pos]
    text_part = decoded_message[first_alnum_pos:last_alnum_pos + 1]
    remaining_part = decoded_message[last_alnum_pos + 1:]

    filtered_text = re.sub(r'[^a-zA-Z0-9]+', ' ', text_part)
    filtered_text = filtered_text.strip()

    final_message = start_part + filtered_text + remaining_part
    print(final_message)
except:
    first_alnum_pos = 0
    last_alnum_pos = len(decoded_message)
    final_message = decoded_message[first_alnum_pos:last_alnum_pos]
    print(final_message)
