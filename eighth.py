import re

t = int(input())
for i in range(t):
    s = input()
    ans = True 
    try:
        r = re.compile(s)
    except re.error:
        ans = False 
    print(ans)
