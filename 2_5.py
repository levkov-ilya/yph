# 2_5_F

# 2_5_F

""" areas = int(input())
i = 0
count = 0
res = 0
while i < areas:
    text = input()
    count = text.count('зайка')
    res += count
    i += 1 
print(res) """

# 2_5_E
""" text = input()
print("YES") if text == text[::-1] else print("NO") """


# 2_5_D

""" text.startswith("##")
text.endswith("@@@") """

""" res_arr = []
while (text := input()) != "":
    if (text[:2] == "##" and text[:-4:-1] == "@@@"):
        pass
    elif text[:2] == "##":
        res_arr.append(text[2:])
    elif text[:-4:-1] == "@@@":
        pass
    else:
        res_arr.append(text)

for _ in res_arr:
    print(_) """

# 2_5_C

""" title_length, title_count = int(input()), int(input())
dots = "..."
i = 0
arr = []
while i < title_count:
    text = input()
    if len(text) > title_length:
        arr.append(text[:title_length - len(dots)] + dots)
    else:
        arr.append(text)
    i += 1

for _ in arr:
    print(_) """


# 2_5_B

""" for x in input():
    print(x) """

# 2_5_A

""" count, i = int(input()), 1

pattern = "абв"
s = 0
while i < count + 1:
    text = input()
    if text[0] not in pattern:
        s += 1
    else:
        pass
    i += 1

print("YES") if not s else print("NO") """


