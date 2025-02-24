import sys
from collections import Counter
from io import StringIO


sample_input = """10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50"""
sys.stdin = StringIO(sample_input)


number_shoes = int(input())
shoe_numbers = [int(x) for x in input().split()]
shoe_counts = Counter(shoe_numbers)

number_customer = int(input())

# print(number_customer)
# print(shoe_counts)

total_price = 0
for _ in range(number_customer):
    size_price_input = input().split()
    shoe_size = int(size_price_input[0])
    shoe_price = int(size_price_input[1])
    if shoe_size in shoe_counts.keys() and shoe_counts[shoe_size] > 0:
        shoe_counts[shoe_size] -= 1
        total_price += shoe_price


print(total_price)
