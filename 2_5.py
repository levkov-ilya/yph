# 2_5_N
nums, pow = input(), int(input())

arr = nums.split(" ")

res_arr = []
for x in arr:
    res_arr.append(str(int(x) ** pow))

res_str = " ".join(res_arr)
print(res_str)

# 2_5_M
""" count = int(input())
arr = []
for x in range(count):
    arr.append(int(input()))

power = int(input())
for x in arr:
    print(x ** power) """

# 2_5_L

""" arr = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

days = int(input())
if days == len(arr):
    for x in arr:
        print(x)
elif days < len(arr):
    for x in arr[:days:]:
        print(x)
else:
    full_days = days // 5
    remain_days = days % 5

    res_arr = arr * full_days + arr[:remain_days:]
    for x in res_arr:
        print(x) """


# 2_5_K

""" count = int(input())
pages = []
for x in range(0, count):
    pages.append(input())

search_word = input()

for x in pages:
    if search_word.lower() in str(x).lower():
        print(x) """


""" def search(arr: list, word: str) -> None:
    for x in arr:
        res = str(x).lower()
        if word in res:
            print(x)

arr = ["сериал шерлок смотреть онлайн"
        , "учебник питона"
        , "мемы"
        , "социальная сеть"
        , "упражнения по питону"
        , "кормовые мыши для питонов"
        , "ответы егэ скачать бесплатно"
        , "компьютерные мыши"]
word = "питон"

search(arr, word) """


# 2_5_J

""" res = []
while (text := input()) != "ФИНИШ":
    text = text.lower()
    text = text.replace(" ", "")
    for x in text:
        res.append(x)

res.sort(reverse=False)

count = 0
letter = ""
for x in res:
    if count < res.count(x):
        count = res.count(x)
        letter = x
print(letter) """

# 2_5_I

""" res = []
while (text := input()) != "":
    if text.startswith("#"):
        pass
    elif ("#" in text) and (text.index("#") != 0):
        res.append(text[:text.index("#"):].rstrip())
    else:
        res.append(text)

for _ in res:
    print(_) """

# 2_5_G

""" areas = int(input())
i = 1
res = []
while i <= areas:
    text = input()
    if "зайка" in text:
        res.append(text.index("зайка") + 1)
    else:
        res.append("Заек нет =(")
    i += 1

for _ in res:
    print(_) """

# 2_5_F
""" a, b = input().split(" ")
print(int(a) + int(b)) """

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


