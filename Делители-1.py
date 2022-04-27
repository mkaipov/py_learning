a = int(input())
b = int(input())
sum_divider = 0
max_divider = 0
for i in range(a, b+1):
    counter = 0
    for j in range(1, i+1):
        if i % j == 0:
            counter += j
        if counter >= sum_divider:
            sum_divider = counter
            max_divider = i
print(max_divider, sum_divider)
