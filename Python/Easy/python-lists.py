from io import StringIO
import sys

# Test Case 1
# sample_input = """12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print"""

# Test Case 2
sample_input = """29
append 1
append 6
append 10
append 8
append 9
append 2
append 12
append 7
append 3
append 5
insert 8 66
insert 1 30
insert 6 75
insert 4 44
insert 9 67
insert 2 44
insert 9 21
insert 8 87
insert 1 75
insert 1 48
print
reverse
print
sort
print
append 2
append 5
remove 2
print"""

original_stdin = sys.stdin

sys.stdin = StringIO(sample_input)
idx = 0
if __name__ == '__main__':
    N = int(input())

    list_to_print = []
    for i in range(N):
        command = input()
        command_to_exec = command.split()

        if command.startswith("insert"):
            list_to_print.insert(int(command_to_exec[1]), int(command_to_exec[2]))
        elif command.startswith("remove"):
            list_to_print.remove(int(command_to_exec[1]))
        elif command.startswith("append"):
            list_to_print.append(int(command_to_exec[1]))
        elif command.startswith("sort"):
            list_to_print.sort()
        elif command.startswith("pop"):
            list_to_print.pop(-1)
        elif command.startswith("reverse"):
            list_to_print.reverse()
        elif command.startswith("print"):
            print(list_to_print)


sys.stdin = original_stdin
