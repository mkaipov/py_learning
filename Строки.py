n = int(input())
list_n = []
list_negative = []
list_zeros = []
list_pozitive = []
while n > 0:
    x = int(input())
    if x < 0:
        list_negative.append(x)
    elif x == 0:
        list_zeros.append(x)
    else:
        list_pozitive.append(x)
    n -= 1

list_n.extend(list_negative)
list_n.extend(list_zeros)
list_n.extend(list_pozitive)
print(*list_n, sep='\n')
