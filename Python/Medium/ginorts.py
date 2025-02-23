# sorted() solution
# def sort_key(c):
#     if c.islower():
#         return (0, c)
#     elif c.isupper():
#         return (1, c)
#     elif c.isdigit():
#         # Check if the digit is odd or even
#         return (2, c) if int(c) % 2 == 1 else (3, c)
# sorted_str = ''.join(sorted(s, key=sort_key))
# print(sorted_str)

s = input().strip()

# test case 1
# s = "Sorting1234"

# brute force manual solution
lower_l = []
upper_l = []
even_l = []
odd_l = []

for x in s:
    if x.islower():
        lower_l.append(x)
    elif x.isupper():
        upper_l.append(x)
    elif x.isdigit():
        if int(x) % 2 == 0:
            even_l.append(x)
        else:
            odd_l.append(x)
lower_l.sort()
upper_l.sort()
even_l.sort()
odd_l.sort()

# print(lower_l)
# print(upper_l)
# print(odd_l)
# print(even_l)
str_to_print = ""

for x in lower_l:
    str_to_print += x
for x in upper_l:
    str_to_print += x
for x in odd_l:
    str_to_print += x
for x in even_l:
    str_to_print += x
print(str_to_print)