from itertools import combinations
word, length = input().split()
word = list(word)
word.sort()
for i in range(1, int(length)+1):
    combo_list = list(combinations(word, i))
    for combo in combo_list:
        print(''.join(combo))
    
    
