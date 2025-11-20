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