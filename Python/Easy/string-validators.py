import sys
from io import StringIO


input_sample = """qA2"""

original_stdin = sys.stdin
sys.stdin = StringIO(input_sample)

if __name__ == '__main__':
    s = input()
    char_found = {
        "alphnum": 0,
        "isalpha": 0,
        "isdigit": 0,
        "islower": 0,
        "isupper": 0
    }

    alphnum_flag = False
    isalpha_flag = False
    isdigit_flag = False
    islower_flag = False
    isupper_flag = False

    for x in s:
        if x.isalnum():
            char_found["alphnum"] += 1

        if x.isalpha():
            char_found["isalpha"] += 1

        if x.isdigit():
            char_found["isdigit"] += 1

        if x.islower():
            char_found["islower"] += 1

        if x.isupper():
            char_found["isupper"] += 1

        if alphnum_flag and isalpha_flag and isdigit_flag and islower_flag and isupper_flag:
            break

    for v in char_found.values():
        if v > 0:
            print(True)
        else:
            print(False)
