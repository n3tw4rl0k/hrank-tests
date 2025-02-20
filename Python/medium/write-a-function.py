import sys
from io import StringIO

orig_stdin = sys.stdin

# test case 1
# input_sample = "5"

# test case 2
input_sample = "2100"

sys.stdin = StringIO(input_sample)


def is_leap(year):
    leap = False

    div_by_4 = year % 4
    div_by_100 = year % 100
    div_by_400 = year % 400
    if div_by_100 == 0 and div_by_400 == 0:
        leap = True

    elif div_by_100 == 0:
        leap = False

    elif div_by_4 == 0:
        leap = True

    return leap


year = int(input())
print(is_leap(year))

sys.stdin = orig_stdin