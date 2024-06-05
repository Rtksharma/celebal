t = int(input())
for i in range(t):
    try:
        a, b = map(int, input().split())
        c = a//b
        print(c)
    except ZeroDivisionError as e:
        print(f'Error Code: {e}')
    except ValueError as a:
        print(f'Error Code: {a}')
