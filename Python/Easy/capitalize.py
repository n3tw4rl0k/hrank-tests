#!/bin/python3

import math
import os
import random
import re
import sys
from io import StringIO


# Complete the solve function below.
def solve(s):
    result = ""
    capitalize_next = True

    for char in s:
        if char.isspace():
            result += char
            capitalize_next = True
        else:
            if capitalize_next:
                result += char.capitalize()
                capitalize_next = False
            else:
                result += char

    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # test case helper
    fptr = sys.stdout
    # test case 1
    # input_sample = "alan ross"
    input_sample = "hello   world  lol"
    orig_stdin = sys.stdin
    sys.stdin = StringIO(input_sample)
    # end of case debug help

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
