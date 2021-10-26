# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
from collections import OrderedDict
n = int(input())
itemdict = OrderedDict()
for i in range(n):
    items = input()
    itemlist = items.split(' ')
    price = int(itemlist[-1])
    item_name = " ".join(itemlist[:-1])
    if itemdict.get(item_name):
        itemdict[item_name] += price
    else:
        itemdict[item_name] = price
        
for key, value in itemdict.items():
    print(key, value)
    