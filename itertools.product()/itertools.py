# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*product(A,B))

# * operator is known as unpacking operator, treats each item of list individually.