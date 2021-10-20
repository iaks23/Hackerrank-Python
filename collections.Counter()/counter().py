import collections
from collections import Counter 

shoes = int(input())
sizes = collections.Counter(map(int, input().split()))
customers = int(input())

total = 0
for i in range(customers):
    size, price = map(int, input().split())
    if(sizes[size]):
        sizes[size] -= 1
        total += price 
print(total)