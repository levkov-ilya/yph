# 2_4_L

n, m = int(input()), int(input())

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print("j", sep=" ")
    print("i", sep=" ")


# 2_4_K

""" count = int(input())
iter = 1
primes = 0
div = 0
while iter <= count:
    num = int(input())
    for i in range(1, num + 1):
        if num % i != 0:
            pass
        else: 
            div += 1
    else:
        if div == 2:
            primes += 1
    div = 0
    iter += 1
print(primes) """

# 2_4_J

""" count = int(input())

print(f"А Б В")
for a in range(1, count):
    for b in range(1, count):
        for c in range(1, count):
            if a + b + c == count:
                print(f"{a} {b} {c}") """


# 2_4_I

""" count = int(input())
i = 0
max_current_num = 0
res = ""
while i < count:
    current_num = input()
    for x in current_num:
        if int(x) >= max_current_num:
            max_current_num = int(x)
    res += str(max_current_num)
    max_current_num = 0
    i += 1
print(res) """

# 2_4_H
""" count = int(input())
i = 0
max_sum_num = 0 
max_sum_name = ""

while i < count:
    name = input()
    num = input()
    sum_num = 0
    for x in num:
        sum_num += int(x)
    # print(f"sum_num = {type(sum_num)}")
    if sum_num >= max_sum_num:
        max_sum_num = sum_num
        max_sum_name = name
    i += 1
print(f"{max_sum_name}") """

# 2_4_F

""" count = int(input())
i = 1
pos = 1
sec = 1
while i <= count:
    sec_cap = i + 2
    while sec <= sec_cap:
        print(f"До старта {sec_cap} секунд(ы)")
        sec_cap -= 1
    print(f"Старт {i}!!!")
    i += 1 """

# 2_4_E
""" count = int(input())
i = 1
all_areas = 0
while i <= count:
    iter = 0
    while ((a := input()) != 'ВСЁ'):
        if a != "зайка":
            continue
        else:
            iter = 1
    all_areas += iter 
    i += 1
print(all_areas) """


""" count = int(input())
i = 1
all_s = 0
iter = 0
while i <= count:
    s = 0
    while ((a := input()) != 'ВСЁ'):
        # print(f"a = '{a}'")
        if a != "зайчик":
            # print(f"Это не зайчик")
            continue
        else:
            s += 1
        if s > 0:
            iter = 1
            # print(f"зайчик №{s}")
    all_s += iter # счетчик всех зайчиков
    i += 1
print(all_s) """

# 2_4_D

""" count, i = int(input()), 1
s = ""
res = 0
while i <= count:
    d = input()
    s += d  
    i += 1
for x in s:
    res += int(x)
print(res)
 """
# 2_4_C
""" max_number = int(input())

row = 1  # номер строки, которую мы собираемся выводить
col = 1  # номер столбца, который мы собираемся выводить
number = 1 # число, которое мы собираемся выводить

while number <= max_number:
    while col <= row and number <= max_number:  
        print(number, end=" ")
        number += 1
        col += 1
    row += 1
    col = 0 """

""" s = 0
v = 0
for i in range(1, 5):
    for j in range(1, i + 1):
        if i == 1:
            print("1", end="")
        else:    
            print(i + s, end="")
            s += 1
    print() """
        
# 2_4_B
""" n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{j} * {i} = {j * i}") """

# 2_4_A
""" n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print() """