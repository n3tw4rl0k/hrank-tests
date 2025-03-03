# Enter your code here. Read input from STDIN. Print output to STDOUT
from io import StringIO
import sys

# test case 1
input_sample = """1 2
abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaxxxxxxxxxx
abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaxxxxxxxxxx
abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbaxxxxxxxxxxy"""
sys.stdin = StringIO(input_sample)

from collections import defaultdict


nm_list = input().split()

n = int(nm_list[0])
m = int(nm_list[1])

# print(n)
# print(m)
def_dict = defaultdict(list)

for _ in range(n):
    line_r = input()
    # print(line_r)
    def_dict["A"].append(line_r)

for _ in range(m):
    line_r = input()
    def_dict["B"].append(line_r)


str_to_print = ""
for x_p, x_v in enumerate(def_dict["B"]):
    for z_p, z_v in enumerate(def_dict["A"]):
        if x_v == z_v:
            str_to_print = str_to_print + str(z_p+1) + " "
    if str_to_print == "":
        print("-1")
    else:
        print(str_to_print.strip())
    str_to_print = ""
