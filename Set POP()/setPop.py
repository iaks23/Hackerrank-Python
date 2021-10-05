n = int(input())
s = set(map(int, input().split()))
commands = int(input())
for i in range(commands):
    choice = input().split()
    if choice[0] == "pop":
        s.pop()
    elif choice[0] == "remove":
        s.remove(int(choice[1]))
    else:
        s.discard(int(choice[1]))

print(sum(s))
