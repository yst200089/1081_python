# input year
# if is leap year
#    print('xxxx is a leap year')
# else
#    print('xxxx is a common year')
#if can't divisible 4 is common year
#else if can divisible 4,but can't divisible 100 is leap year
#else if can divisible 100,but can't divisible 400 is common year
#else if can divisible 400 is leap year
year = int(input())
if year % 4 != 0 :
    print('common year')
elif year % 100 != 0 :
    print('leap year')
elif year % 100 == 0 and year % 400 != 0 :
    print('common year')
elif year % 400 == 0 :
    print('leap year')