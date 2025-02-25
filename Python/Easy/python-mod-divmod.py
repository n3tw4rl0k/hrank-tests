# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())

result_obj = divmod(a, b)
print(result_obj[0])
print(result_obj[1])
print(result_obj)