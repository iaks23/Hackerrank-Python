# Enter your code here. Read input from STDIN. Print output to STDO
m, a, n, b = int(input()), set(map(int, input().split())),int(input()), set(map(int, input().split()))

c = a.difference(b)
d = b.difference(a)
e = c.union(d)
print(*sorted(e), sep='\n')
