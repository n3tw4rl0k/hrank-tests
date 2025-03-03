from io import StringIO
import sys

# test case 1
input_sample = """5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   """

# test case 1
# input_sample = """5
# MARKS      CLASS      NAME       ID
# 92         2          Calum      1
# 82         5          Scott      2
# 94         2          Jason      3
# 55         8          Glenn      4
# 82         2          Fergus     5"""

sys.stdin = StringIO(input_sample)

from collections import namedtuple
n_line = int(input())
fields = input().split()
Student = namedtuple('Student', fields)
total_marks = 0
for _ in range(n_line):
    field_values = input().split()
    student = Student(*field_values)
    total_marks += int(student.MARKS)
print('{:.2f}'.format(total_marks/n_line))