# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
from collections import Counter 
size = int(input())
occupencies = collections.Counter(map(int, input().split()))
for x in occupencies:
    if(occupencies[x]==1):
        print(x)

    
