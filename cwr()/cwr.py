# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement as cwr
word, length = input().split()
combolist = list(cwr(sorted(word), int(length)))
for combo in combolist:
    print(''.join(combo))

    
    
