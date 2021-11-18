# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
regex_pattern = r"^[789]\d{9}$"

for i in range (n):
    if(re.match(regex_pattern, input())):
        print("YES")
    else:
        print("NO")