a, b, c=int(input('Введите число a: ')), int(input('Введите число b: ')), int(input('Введите число c: '))
num1=(a**2+b**2)/(3*b-4)
num2=(4*c**5)/6
print(f'Целая часть равна: {num1//num2}')
print(f'Остаток от деления равен: {num1%num2}')