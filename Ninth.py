n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    c = input().split()
    if len(c) == 1:
        getattr(s, c[0])()
    else:
        getattr(s, c[0])(int(c[1]))
print(sum(s))
