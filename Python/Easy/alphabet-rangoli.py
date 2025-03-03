from io import StringIO
import sys

# test case 1
input_sample = "26"
sys.stdin = StringIO(input_sample)


def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(size - 1, -1, -1):
        letters = [alphabet[j] for j in range(size - 1, i - 1, -1)]
        letters += [alphabet[j] for j in range(i + 1, size)]
        line = '-'.join(letters)
        width = 4 * size - 3
        print(line.center(width, '-'))

    for i in range(1, size):
        letters = [alphabet[j] for j in range(size - 1, i - 1, -1)]
        letters += [alphabet[j] for j in range(i + 1, size)]
        line = '-'.join(letters)
        width = 4 * size - 3
        print(line.center(width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)