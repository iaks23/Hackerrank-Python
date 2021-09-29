from __future__ import division

def average(array):
    # your code goes here
    array = set(array)
    #return float("{0:.3f}".format(sum(array)/len(array)))
    return format(sum(array)/len(array), ".3f")

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
