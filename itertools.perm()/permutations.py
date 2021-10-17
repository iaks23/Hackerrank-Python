# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

word, length = input().split()
wordlist = list(permutations(word, int(length)))
wordlist.sort()
for word in wordlist:
    print("".join(word))