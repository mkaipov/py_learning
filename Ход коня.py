x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
x = x1 - y1
y = x2 - y2
if abs(x) == 1 and abs(y) == 2:
    print('YES')
elif abs(x) == 2 and abs(y) == 1:
    print('YES')
else:
    print('NO')
