# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
date = input()
datelist = date.split(" ")
month = int(datelist[0])
day = int(datelist[1])
year = int(datelist[2])
print(calendar.day_name[calendar.weekday(year,month,day)].upper())