# https://stepik.org/lesson/265082/step/8?unit=246030
a = int(input())
b = int(input())
c = str(input())

if b == 0 and c == '/':
    print('На ноль делить нельзя!')
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
else:
    print('Неверная операция')
