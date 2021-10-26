# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(map(int, input().split()))
others = int(input())
for i in range(others):
    cmd, _ = input().split(' ')
    b = set(map(int, input().split()))
    if cmd=='intersection_update':
        a.intersection_update(b)
    elif cmd=='symmetric_difference_update':
        a.symmetric_difference_update(b)
    elif cmd=='update':
        a.update(b)
    else:
        a.difference_update(b)

print(sum(a))
    