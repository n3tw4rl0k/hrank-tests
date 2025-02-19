from io import StringIO
import sys

# test case 1
sample_input = """2
1 2"""

# notes
# h-rank has a bug for this test-case
# it only works out with pypy3 , but not with python3,
# hash() returns some other crazy negative number if use python3

orig_stdin = sys.stdin
sys.stdin = StringIO(sample_input)

if __name__ == '__main__':
    space_len = int(input())
    int_tuple = tuple(int(x) for x in str(input()).split())
    print(hash(int_tuple))

sys.stdin = orig_stdin