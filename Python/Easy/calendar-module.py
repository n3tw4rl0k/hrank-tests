# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar


month, day, year = map(int, input().split())

weekday_number = calendar.weekday(year, month, day)

weekday_names = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
weekday_name = weekday_names[weekday_number]

print(weekday_name)