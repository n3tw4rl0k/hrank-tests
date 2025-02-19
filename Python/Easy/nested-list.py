from io import StringIO
import sys


# test case 1
sample_input="""5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39"""

# test case 2
# sample_input="""5
# Harsh
# 20
# Beria
# 20
# Varun
# 19
# Kakunami
# 19
# Vikas
# 21"""

original_stdin = sys.stdin

sys.stdin = StringIO(sample_input)

def sort_key(item):
    return item[1], item[0]

if __name__ == '__main__':
    list_orig = []
    max_score = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_orig.append([name, score])

    list_orig.sort(key=sort_key, reverse=False)

    min_score = list_orig[0][1]

    nd_score = 0
    list_names = []
    lock_found = False
    # the test assumes there is always a second student so we can start from the second position
    for x in list_orig[1::]:
        # check to see if x[1]-score is greater than the min score i recorded earlier,
        # and mark with a lock that we found it
        # the lock and this comparison because there can be multiple lowest score OR multiple second lowest score...
        if x[1] > min_score and not lock_found:
            list_names.append(x[0])
            nd_score = x[1]
            lock_found = True
        elif x[1] == nd_score and lock_found and x[0] not in list_names:
            list_names.append(x[0])
    list_names.sort()
    for name_st in list_names:
        print(name_st)

sys.stdin = original_stdin
