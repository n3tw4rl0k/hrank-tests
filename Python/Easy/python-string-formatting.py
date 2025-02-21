import sys
from io import StringIO


input_sample = """17"""

original_stdin = sys.stdin
sys.stdin = StringIO(input_sample)

def print_formatted(number):
    width = len(f"{number:b}")
    for i in range(1, number + 1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)