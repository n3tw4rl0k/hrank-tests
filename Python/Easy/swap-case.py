from io import StringIO
import sys

#test case 1
input_sample = """HackerRank.com presents "Pythonist 2"."""
sys.stdin = StringIO(input_sample)

def swap_case(s):
    str_to_ret = ""
    for x in s:
        if x .isupper():
            str_to_ret += x.lower()
        elif x .islower():
            str_to_ret += x.upper()
        else:
            str_to_ret += x
    return str_to_ret

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)