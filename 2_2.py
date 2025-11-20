# 2_2_T
str_1, str_2, str_3 = input(), input(), input()

a = []
if 'зайка' in str_1:
    a.append(str_1)
if 'зайка' in str_2:
    a.append(str_2)
if 'зайка' in str_3:
    a.append(str_3)

print(min(a), len(min(a)))
# 2_2_S
""" x, y = float(input()), float(input()) 
if (x ** 2 + y ** 2) ** 0.5 > 10:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
elif x >= 0 and y >= 0 and (x ** 2 + y ** 2) ** 0.5 <= 5:
    print('Опасность! Покиньте зону как можно скорее!')
elif -4 <= x < 0 and 5 >= y >= 0:
    print('Опасность! Покиньте зону как можно скорее!')
elif -7 <= x < -4 and 5 >= y >= 0 and 5 * x - 3 * y > -35:
    print('Опасность! Покиньте зону как можно скорее!')
elif 0.25 * x ** 2 + 0.5 * x - 8.75 <= y <= 0:
    print('Опасность! Покиньте зону как можно скорее!')
else:
    print('Зона безопасна. Продолжайте работу.')
 """
# 2_2_P
""" a, b, c = int(input()), int(input()), int(input())

hypotenuse = max(a, b, c) 
side_1 = min(a, b, c)
side_2 = a + b + c - int(hypotenuse) - int(side_1)

if hypotenuse * hypotenuse == side_1 * side_1 + side_2 * side_2:
    print("100%")
elif hypotenuse * hypotenuse > side_1 * side_1 + side_2 * side_2:
    print("велика")
else:
    print("крайне мала") """


# 2_2_Q
""" a, b, c = float(input()), float(input()), float(input())
if not a and not b and not c:
    print('Infinite solutions')
elif not a and not b and c or b ** 2 < 4 * a * c:
    print('No solution')
elif b ** 2 == 4 * a * c:
    print(f'{-b / (2 * a):.2f}')
elif not a:
    print(f'{-c / b:.2f}')
else:
    roots = [(-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)]
    roots.sort()
    print(f'{roots[0]:.2f} {roots[1]:.2f}') """

# 2_2_P
""" p, v, t = int(input()), int(input()), int(input())

p_name, v_name, t_name = 'Петя', 'Вася', 'Толя'

winner = max(p, v, t)
looser = min(p, v, t)
second = p + v + t - winner - looser

if winner == p:
    winner_name = p_name
    if second == v:
        second_name = v_name
        looser_name = t_name
    else:
        second_name = t_name
        looser_name = v_name 
elif winner == v:
    winner_name = v_name
    if second == p:
        second_name = p_name
        looser_name = t_name
    else:
        second_name = t_name
        looser_name = p_name
else:
    winner_name = t_name
    if second == p:
        second_name = p_name
        looser_name = v_name
    else:
        second_name = v_name
        looser_name = p_name

print(f"{'':^8}{winner_name:^8}{'':^8}")
print(f"{second_name:^8}{'':^8}{'':^8}")
print(f"{'':^8}{'':^8}{looser_name:^8}")
print(f"{'II':^8}{'I':^8}{'III':^8}")
 """

# 2_2_O
""" num_1, num_2 = int(input()), int(input())

num_1_max = int(max(str(num_1)))
num_1_min = int(min(str(num_1)))

num_2_max = int(max(str(num_2)))
num_2_min = int(min(str(num_2)))

max_d = max(num_1_max, num_2_max, num_1_min, num_2_min)
min_d = min(num_1_max, num_2_max, num_1_min, num_2_min)

mid_sum = 0
if num_1_max > num_2_max:
    mid_sum = num_2_max
else:
    mid_sum = num_1_max

if num_1_min > num_2_min:
    mid_sum += num_1_min
else:
    mid_sum += num_2_min

mid_d = mid_sum % 10

print(f"{max_d}{mid_d}{min_d}") """


# 2_2_N
""" num = int(input())

num_1 = num // 100 % 10
num_2 = num % 100 // 10
num_3 = num % 10

max_num = max(num_1, num_2, num_3)
min_num = min(num_1, num_2, num_3)
mid_num = num_1 + num_2 + num_3 - max_num - min_num

if min_num > 0:
    print(f"{min_num}{mid_num} {max_num}{mid_num}")
elif mid_num > 0: 
    print(f"{mid_num}{min_num} {max_num}{mid_num}") """

# 2_2_M
""" e, g, h = int(input()), int(input()), int(input())

e_1 = e % 100 // 10
e_2 = e % 10

g_1 = g % 100 // 10
g_2 = g % 10

h_1 = h % 100 // 10
h_2 = h % 10

if (e_1 == g_1) and (e_1 == h_1):
    print(e_1)
elif (e_2 == g_2) and (e_2 == h_2):
    print(e_2)
 """

# 2_2_L
""" a, b, c = int(input()), int(input()), int(input())

max_num = max(a, b, c)
min_num = min(a, b, c)
mid_num = a + b + c - max_num - min_num

if max_num < mid_num + min_num:
    print("YES")
else:
    print("NO") """

# 2_2_K
""" num = int(input())

num_1 = num // 100 % 10
num_2 = num % 100 // 10
num_3 = num % 10
max_num = max(num_1, num_2, num_3)
min_num = min(num_1, num_2, num_3)
mid_num = num_1 + num_2 + num_3 - max_num - min_num

if max_num + min_num == int(mid_num) * 2:
    print("YES")
else:
    print("NO") """


# 2_2_J
""" pwd = int(input())

first_sum = ((pwd % 100 // 10) + (pwd % 10))
second_sum = ((pwd // 100 % 10) + (pwd % 100 // 10))
if first_sum <= second_sum:
    print(f"{second_sum}{first_sum}")
else:
    print(f"{first_sum}{second_sum}") """

# 2_2_I
""" name_1, name_2, name_3 = input(), input(), input()
first = min(name_1, name_2, name_3)
print(first) """


# 2_2_H
""" area = input()

if "зайка" in area:
    print("YES")
else:
    print("NO")
 """
# 2_2_G
""" num = int(input())

num_1 = str(num // 1000)
num_2 = str(num // 100 % 10)
num_3 = str(num % 100 // 10)
num_4 = str(num % 10)

if num == int(num_4 + num_3 + num_2 + num_1):
    print("YES")
else:
    print("NO") """

# 2_2_F
""" year = int(input())

if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    print("YES")
else:
    print("NO")
 """
# 2_2_E
""" petya = 7
vasya = 6
petya -= 3
vasya += 3
petya += 2
vasya += 5
vasya -= 2

n, m = int(input()), int(input())
petya += n
vasya += m

if petya > vasya:
    print("Петя")
else:
    print("Вася") """

# 2_2_D
""" p, v, t = int(input()), int(input()), int(input())

p_name, v_name, t_name = 'Петя', 'Вася', 'Толя'

winner = max(p, v, t)
looser = min(p, v, t)
second = p + v + t - winner - looser

if winner == p:
    winner_name = p_name
    if second == v:
        second_name = v_name
        looser_name = t_name
    else:
        second_name = t_name
        looser_name = v_name 
elif winner == v:
    winner_name = v_name
    if second == p:
        second_name = p_name
        looser_name = t_name
    else:
        second_name = t_name
        looser_name = p_name
else:
    winner_name = t_name
    if second == p:
        second_name = p_name
        looser_name = v_name
    else:
        second_name = v_name
        looser_name = p_name


print(f"1. {winner_name}\n2. {second_name}\n3. {looser_name}")  """

""" # 2_2_D
petya_speed, vasya_speed, tolya_speed = int(input()), int(input()), int(input())
winner_speed = max(petya_speed, vasya_speed, tolya_speed)
loser_speed = min(petya_speed, vasya_speed, tolya_speed)
if winner_speed == petya_speed:
    winner = 'Петя'
    if loser_speed == tolya_speed:
        loser, second = 'Толя', 'Вася'
    else:
        loser, second = 'Вася', 'Толя'       
elif winner_speed == tolya_speed:
    winner = 'Толя'
    if loser_speed == petya_speed:
        loser, second = 'Петя', 'Вася'
    else:
        loser, second = 'Вася', 'Петя'
else:
    winner = 'Вася'
    if loser_speed == tolya_speed:
        loser, second = 'Толя', 'Петя'
    else:
        loser, second = 'Петя', 'Толя'
for place in range(1, 4):
    print(f'{place}. {(winner, second, loser)[place-1]}') """



# 2_2_C
""" petya, vasya, tolya = int(input()), int(input()), int(input()) 
if (petya > vasya) and (petya > tolya):
    print('Петя')
elif (vasya > petya) and (vasya > tolya):
    print('Вася')
else:
    print('Толя') """

# 2_2_B
""" petya, vasya = int(input()), int(input())
if petya > vasya:
    print('Петя')
else:
    print('Вася') """

# 2_2_A
""" name = input()
mood = input()
print("Как Вас зовут?")
print(f"Здравствуйте, {name}!")
print("Как дела?")
if mood == "хорошо":
    print("Я за Вас рада!")
else: 
    print("Всё наладится!") """