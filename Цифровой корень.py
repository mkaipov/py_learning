n = int(input())
while n > 9:
    sum_n = 0
    while n > 0:
        last_digit = n % 10
        sum_n += last_digit
        n //= 10
    n = sum_n
print(n)
