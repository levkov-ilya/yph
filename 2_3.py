# 2_3_R



# 2_3_Q

""" text = input()
res = ""
i = 0
while i < 1:
    for x in text:
        if int(x) % 2 != 0:
            res += x
        else:
            res += ""
    i += 1
print(res) """


# 2_3_P

""" text = input()
while text == text[::-1]:
    print("YES")
    break
else:
    print("NO")
 """
# 2_3_O

""" n = int(input())
count = 0
for i in range(0, n):
    s = input()
    if "зайка" in s:
        count += 1
    i += 1
print(count) """

s = "березка елочка зайка волк березка"
""" if "зайка" in s:
    print("ok")
else:
    print("not ok") """
""" 
березка елочка зайка волк березка
сосна сосна сосна елочка грибочки медведь
сосна сосна сосна белочка сосна белочка """


# 2_3_N
""" n = int(input())
is_prime = True
if n == 1 or (n > 2 and n % 2 == 0):
    is_prime = False
else:
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print("YES")
else:
    print("NO") """


# 2_3_N

""" d, prime = int(input()), True

for div in range(2, d // 2):
    if (d % div == 0) or (d == 1):
        prime = False

print("YES") if prime else print("NO") """

""" d, count = int(input()), 0

for div in range(2, d // 2):
    if d % div == 0:
        count += 1
if d != 1 and count == 0:
    print("YES")
else:
    print("NO") """

""" d = int(input())

count_div = 0
for div in range(1, d+1):
    if d % div == 0:
        count_div +=1
if d != 1 and count_div == 2:
    print("YES")
else:
    print("NO") """

""" d = int(input())
count_div = 0

if d >= 2:
    for div in range(2, d / 2):
        if d % div == 0:
            count_div += 1
    if count_div == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
 """
# 2_3_N
""" n = int(input())

for i in range(1, n+1):
    if n == 1:
        print("NO")
    else:
        if () and (n != i):
            print("YES")
 """

# 2_3_M
""" n = int(input())
i = 0
min_name = ""
while i < n:
    if i == 0:
        input_name = input()
        min_name = input_name
    else:
        name = input()
        if name < min_name:
            min_name = name
    i += 1
print(min_name) """

""" n = int(input())
min_name = ""
for i in range(0, n):
    if i == 0:
        input_name = input()
        min_name = input_name
    else:
        name = input()
        if name < min_name:
            min_name = name
    i += 1
print(min_name)
 """


# 2_3_L
""" d = input()
d_max = 0
for i in d:
    if int(i) >= d_max:
        d_max = int(i)
print(d_max) """

# 2_3_K
""" d = input()
d_len = len(d)
i, sum = 0,0
while i < d_len:
    sum += int(d[i])
    i += 1

print(sum) """

""" 
d, i, sum = list(input()), 0, 0
for i in d:
    sum += int(i)
print(sum) 
"""

# 2_3_J
""" n, s, e, w = 0, 0, 0, 0
x, y = 0, 0

# while (route := input() != "СТОП"):
while True:
    route = str(input())
    if route == 'СТОП':
        break
    step = int(input())

    match route:
        case 'СЕВЕР':
            n += step
        case 'ЮГ':
            s += step
        case 'ВОСТОК':
            e += step
        case 'ЗАПАД':
            w += step

x = -w + e
y = -s + n   
# print(f"{n} {s} {e} {w}")
print(f"{y}\n{x}") """

"""     while (step := int(input())): 
        if route == "СЕВЕР":
            n += step
        elif route == "ЮГ":
            s += step
        elif route == "ВОСТОК":
            e += step
        elif route == "ЗАПАД":
            w += step
        

print(f"{n} {s} {e} {w}")
 """
# 2_3_I
""" d = int(input())
f = 1

for i in range(1, d + 1):
    if d == 0:
        f = 1
    else:
        f *= i
print(f)  """

# 2_3_H
""" text, counter = input(), int(input())
for i in range(counter):
    print(text) """

# 2_3_F

# 2_3_E

""" result = 0.
while (price := float(input())): # не понял почему не сравниваем с нулем
    if price >= 500:
        price *= 0.9
    result += price
print(result)
 """
# 2_3_D
""" a, b = int(input()), int(input())

if a <= b:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    for i in range(a, b - 1, -1):
        print(i, end=" ")
 """
# 2_3_C
""" a, b = int(input()), int(input())

for i in range(a, b + 1, 1):
    print(i, end=" ")
 """

# 2_3_B
""" counter = 0
while (string := input()) != 'Приехали!':
    if 'зайка' in string:
        counter += 1 
print(counter) """

# 2_3_A
""" while input() != 'Три!':
    print("Режим ожидания...")
print("Ёлочка, гори!") """