# Enter your code here. Read input from STDIN. Print output to STDOUT
test_case = int(input())
for i in range(test_case):
    x, a, y, b = int(input()), set(input().split()), int(input()), set(input().split())
    print(a.issubset(b))

    