# Enter your code here. Read input from STDIN. Print output to STDOUT
count = int(input())
countries = set()
for i in range(0, count):
    country = input()
    countries.add(country)
print(len(countries))