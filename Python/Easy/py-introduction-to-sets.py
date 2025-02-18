def average(array):
    set_arr = set(arr)
    return sum(set_arr) / len(set_arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)