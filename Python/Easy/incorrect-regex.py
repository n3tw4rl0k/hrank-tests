import re
import sys
from io import StringIO


# test case 1
input_sample = """2
.*\+
.["""
sys.stdin = StringIO(input_sample)


n_str = int(input())

for n in range(n_str):
    input_str = input()
    try:
        re.compile(input_str)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)
