#!/bin/python3

import math


if __name__ == '__main__':
    n = int(input().strip())
    if math.fmod(n, 2) != 0:
        print("Weird")
    elif n > 20 and math.fmod(n, 2) == 0:
        print("Not Weird")
    elif 6 <= n <= 20 and math.fmod(n, 2) == 0:
        print("Weird")
    elif 2 <= n <= 5 and math.fmod(n, 2) == 0:
        print("Not Weird")
