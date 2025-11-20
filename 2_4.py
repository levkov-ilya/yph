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