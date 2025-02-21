import sys
from io import StringIO

# test case 1
# input_sample = """ABCDCDC
# CDC"""

# test case 2
# input_sample = """I am an Indian, by birth.
# Birth"""

# test case 3
input_sample = """ininini
ini"""

original_stdin = sys.stdin
sys.stdin = StringIO(input_sample)


# something seems wrong here, but this is how i have solved this "manually" searching for the string
def count_substring(string, sub_string):
    count_ss = 0
    for x in range(len(string)):
        flag = True
        try:
            for y, z in enumerate(sub_string):
                # print(string[x])
                if z != string[x+y]:
                    flag = False
            if flag == True:
                count_ss += 1
        except:
            pass

    return count_ss


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
