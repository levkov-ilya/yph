# 2_T
weight, price, price_1, price_2 = int(input()), int(input()), int(input()), int(input())
weight_1 = int((price - price_2) * weight / (price_1 - price_2))
weight_2 = weight - weight_1
print(weight_1, weight_2)

# 2_S 
""" item, price, weight, money = input(), int(input()), int(input()), int(input())
headings = ['Товар:', 'Цена:', 'Итого:', 'Внесено:', 'Сдача:']
values = [item, f'{weight}кг * {price}руб/кг', f'{weight * price}руб', f'{money}руб', f'{money - weight * price}руб']
print('Чек'.center(35, '='))
for i in range(len(headings)):
    print(f"{headings[i] : <10}{values[i] : >25}")
print('=' * 35) """

# 2_R
""" a, b = int(input(), 2), int(input())
print(b - a) """

# 2_Q
# a, b = int(input()), int(input(), 2)
# print(int(input()) + int(input(), 2))

# 2_P
""" a, b, c = int(input()), int(input()), int(input())
res = (b - a) / c
print(f"{res:.2f}") """

# 2_O
""" hours, minutes, delivery_minutes = int(input()), int(input()), int(input())
all_minutes = (minutes + delivery_minutes) % 60
all_hours = (hours + (minutes + delivery_minutes) // 60) % 24
f_all_hours = str((all_hours + 100))[1:]
f_all_minutes = str((all_minutes + 100))[1:]
print(f"{f_all_hours}:{f_all_minutes}") """

# 2_N
""" r, g, b = int(input()), int(input()), int(input())
print(r + b + 1) """

# 2_M
""" n, m = int(input()), int(input())
res_1 = m // n
res_2 = m % n
print(f"{res_1}\n{res_2}") """


# 2_L
""" a, b = int(input()), int(input())

a_1 = a // 100
a_2 = int((a % 100 - a % 10) / 10)
a_3 = a % 10

b_1 = b // 100
b_2 = int((b % 100 - b % 10) / 10)
b_3 = b % 10

c_3 = str((a_3 + b_3) % 10)
c_2 = str((a_2 + b_2) % 10)
c_1 = str((a_1 + b_1) % 10)

print(int(c_1 + c_2 + c_3)) """


# res = int(float(str(c_1 + c_2 + c_3)) * 10)
# print(res)




""" s = "ilya"
a = 10
print(f"{s:1<10}", sep="\t")
print(f"{s:0>10}")
print(f"{s:0^10}") """

""" arr = [1, '2', 542, '234', 'ilya']
name, *_, s = arr

print(f"{name}, {s}")
print(*_) """

# 2_K
""" num = int(input())
num_1 = num // 1000 # первый разряд
num_2 = num // 100 % 10 # второй разряд
num_3 = num % 100 // 10 # третий разряд
num_4 = num % 10 # четвертый разряд """

""" num = int(input())
num_1 = num // 1000
num_2 = num // 100 % 10
num_3 = num % 100 // 10
num_4 = num % 10

print(int(f'{num_2}{num_1}{num_4}{num_3}')) """

# 2_J
""" name, wardrobe_num = input(), int(input())
group_num = int(wardrobe_num // 100)
bed_num = int(wardrobe_num // 10 % 10)
kid_num = int(wardrobe_num % 100 % 10)
print(f'Группа №{group_num}.')
print(f'{kid_num}. {name}.')  
print(f'Шкафчик: {wardrobe_num}.')
print(f'Кроватка: {bed_num}.')
 """


# 2_I
# n, m = int(input()), int(input())
""" print(int(int(input()) * int(input()) / 2))
 """


# 2_H
""" count, execution = int(input()), input()
print(('Я больше никогда не буду писать "' + execution + '"!\n') * count) 
 """
# 2_G
""" print('Купи слона!\n' * int(input())) """


# 2_F
""" name, price, weight, cash = input(), int(input()), int(input()), int(input())

print(f'Чек')
print(f'{name} - {weight}кг - {price}руб/кг')
print(f'Итого: {price * weight}руб')
print(f'Внесено: {cash}руб')
print(f'Сдача: {cash - price * weight}руб') """