n = int(input())
max_digit = 0
while abs(n) < 10**6 + 1:
    if n > 0:
        if n % 3 == 0:
            max_digit = n / 3
            break
        else:
            n -= 1
    elif n < 0:
        if n % 3 == 0:
            max_digit = n / 3
            break
        else:
            n += 1
if max_digit == 0:
    print('NO')
else:
    print(int(max_digit))