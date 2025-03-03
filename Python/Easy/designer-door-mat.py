def print_door_mat(n, m):
    pattern = ".|."

    for i in range(n // 2):
        print((pattern * (2 * i + 1)).center(m, "-"))

    print("WELCOME".center(m, "-"))

    for i in range(n // 2 - 1, -1, -1):
        print((pattern * (2 * i + 1)).center(m, "-"))


n, m = map(int, input().split())

print_door_mat(n, m)