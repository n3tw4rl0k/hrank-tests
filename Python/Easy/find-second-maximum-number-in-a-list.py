# manually finding the highest 2 numbers, LLMs currently do not know how to solve this problem!
# all LLMs solve it by providing a wrong answer when asked to find this manually without using sort or sorted.
# 18/feb/2025
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_l = list(arr)

    key_max_1 = arr_l[0]
    key_max_2 = arr_l[0]
    flag = False
    for number in arr_l:
        if number > key_max_1 and number != key_max_2:
            key_max_2 = key_max_1
            key_max_1 = number
        elif number != key_max_2 and number < key_max_1 and not flag:
            key_max_2 = number
            flag = True
        elif number > key_max_2 and number != key_max_1:
            key_max_2 = number

    print(key_max_2)