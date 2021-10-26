n, a, m, b = int(input()), set(map(int, input().split())),int(input()), set(map(int, input().split()))

intersected_set = a.intersection(b)
print (len(intersected_set))
    