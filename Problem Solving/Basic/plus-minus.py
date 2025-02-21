#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# test case 1
# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]


def plusMinus(arr):
    map_vals = {
        "pos": 0,
        "neg": 0,
        "zer": 0
    }

    for x in arr:
        if x > 0:
            map_vals["pos"] += 1
        elif x < 0:
            map_vals["neg"] += 1
        else:
            map_vals["zer"] += 1

    proc_1 = float(map_vals["pos"] / len(arr))
    proc_2 = float(map_vals["neg"] / len(arr))
    proc_3 = float(map_vals["zer"] / len(arr))
    print(f"{proc_1:.6f}")
    print(f"{proc_2:.6f}")
    print(f"{proc_3:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
