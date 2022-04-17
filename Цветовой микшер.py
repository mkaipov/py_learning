colour_a = input()
colour_b = input()
if colour_a == 'красный' and colour_b == 'синий' or colour_a == 'синий' and colour_b == 'красный':
    print('фиолетовый')
elif colour_a == 'красный' and colour_b == 'желтый' or colour_a == 'желтый' and colour_b == 'красный':
    print('оранжевый')
elif colour_a == 'синий' and colour_b == 'желтый' or colour_a == 'желтый' and colour_b == 'синий':
    print('зеленый')
else:
    if colour_a == 'синий' and colour_b == 'синий':
        print('синий')
    elif colour_a == 'красный' and colour_b == 'красный':
        print('красный')
    elif colour_a == ';желтый' and colour_b == 'желтый':
        print('желтый')
    else:
        print('ошибка цвета')
