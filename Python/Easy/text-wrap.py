import textwrap


def wrap(string, max_width):
    str_tp = ""
    list_str = textwrap.wrap(string, width=max_width)
    for x in list_str:
        str_tp = str_tp + x + "\n"
    return str_tp


if __name__ == '__main__':
    # string, max_width = input(), int(input())
    string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    max_width = 4
    result = wrap(string, max_width)
    print(result)