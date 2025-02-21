import sys
from io import StringIO


input_sample = """3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika"""

original_stdin = sys.stdin
sys.stdin = StringIO(input_sample)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    obtain_query_marks = student_marks[query_name]
    f_p = sum(obtain_query_marks) / len(obtain_query_marks)
    print(f"{f_p:.2f}")
