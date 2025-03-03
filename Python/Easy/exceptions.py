from io import StringIO
import sys

#test case 1
input_sample = """3
1 0
2 $
3 1"""

sys.stdin = StringIO(input_sample)

input_n = int(input())
for _ in range(input_n):
    a, b = [x for x in input().split()]
    try:
        print(int(a)//int(b))
    except ValueError as e:
        print("Error Code:", e)
    except ZeroDivisionError as e:
        print("Error Code:", e)