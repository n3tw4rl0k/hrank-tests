def mutate_string(string, position, character):
    split_str = list(string)
    split_str[position] = character
    upd_str = "".join(split_str)
    return upd_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)