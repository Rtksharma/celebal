from collections import Counter

input()
map_s = Counter(map(int, input().split()))

e = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    st = map_s[size]
    if st > 0:
        e+= price
        map_s[size] -= 1
    
print(e)
