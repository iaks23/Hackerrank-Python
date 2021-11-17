# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    N = input().strip()
    print(bool(re.match('^[+-.]?[0-9]*[\.]{1}[0-9]+$', N)))
