# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
from collections import defaultdict
n, m = map(int, input().split())
A, B = list(), list()
for i in range (n):
    number = input()
    A.append(number)
for i in range(m):
    number = input()
    B.append(number)

d = defaultdict(list)
for i in range(n):
    d[A[i]].append(i+1)  

for x in B:
    if x in d.keys():
        print(*d[x])
    else:
        print(-1)

    



    

    