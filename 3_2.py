# 3_2_M

food_amount = int(input)
food_names = {}



""" food_amount = int(input())
food_names = []
for _ in range(food_amount):
    food_names.append(input())

days = int(input())

for _ in range(days):
    food_amount_in_day = int(input())
    for day in food_amount_in_day: """




# 3_2_L
""" n = int(input())

names = []
for _ in range(n):
    names.append(input())

counter = {}
for name in names:
    if name not in counter:
        counter[name] = 1
    else:
        counter[name] += 1

count = 0
res = []
for key, value in counter.items():
    if value > 1:
        res.append(key + " - " + str(value))

res = sorted(res)

if len(res) > 0:
    for x in res:
        print(x)
else:
    print("Однофамильцев нет") """

# print(count)


# 3_2_K

""" n = int(input())

names = []
for _ in range(n):
    names.append(input())

counter = {}
for name in names:
    if name not in counter:
        counter[name] = 1
    else:
        counter[name] += 1

count = 0
for value in counter.values():
    if value > 1:
        count += value

print(count)
 """


# 3_2_J
""" TRANS_DICT = {
    "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", 
    "Ё": "E", "Ж": "ZH", "З": "Z", "И": "I", "Й": "I", "К": "K", 
    "Л": "L", "М": "M", "Н": "N", "О": "O", "П": "P", "Р": "R", 
    "С": "S", "Т": "T", "У": "U", "Ф": "F", "Х": "KH", "Ц": "TC", 
    "Ч": "CH", "Ш": "SH", "Щ": "SHCH", "Ы": "Y", "Э": "E", "Ю": "IU", 
    "Я": "IA", "Ь": "", "Ъ": ""
}

result = ""
for char in input():
    char_copy = char.upper()
    if char_copy in TRANS_DICT:
        if char.isupper():
            char = TRANS_DICT[char_copy].capitalize()
        else:
            char = TRANS_DICT[char_copy].lower()
    result += char

print(result) """

# 3_2_I

""" areas = ""
while True:
    area = input()
    if area == "":
        break
    else:
        areas += area + " "
areas = areas.strip()
areas_list = list(areas.split())

counter = {}
for x in areas_list:
    if x not in counter:
        counter[x] = 1
    else:
        counter[x] += 1

for key, value in counter.items():
    print(f"{key} {value}") """

# 3_2_H

""" new_list = []

child_num = int(input()) 

for x in range(child_num):
    rec = input()
    new_list.append(rec)

porridge = input()

result = []

for x in new_list:
    if porridge in x:
        pos = str(x).index(" ")
        result.append(x[:pos:])

result = sorted(result)

if len(result) == 0:
    print("Таких нет")
else:
    for x in result:
        print(x)
 """        
# 3_2_G
""" MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' '
}
text = input()
res_list = list(text.upper())
res_list_morse = []

for letter in res_list:
    for key in MORSE_CODE_DICT: 
        if letter == key:
            res_list_morse.append(MORSE_CODE_DICT[key])

for key in res_list_morse:
    if key == " ":
        print()
    else:
        print(key + " ", end="")
print()
 """

# 3_2_F

""" porridge_1_count, porridge_2_count = int(input()), int(input())

res_set = set()
res_list = list()
for x in range(porridge_1_count + porridge_2_count):
    s = input()
    res_set.add(s)
    res_list.append(s)

result = set()
count = 0
for x in res_list:
    if res_list.count(x) > 1:
        pass
    else:
        result.add(x)

if len(result) > 0:
    result_list = list(sorted(result))
    for x in result_list:
        print(x)
else:
    print("Таких нет") """

# 3_2_E

""" porridge_1_count, porridge_2_count = int(input()), int(input())

res_set = set()
res_list = list()
for x in range(porridge_1_count + porridge_2_count):
    s = input()
    res_set.add(s)
    res_list.append(s)

result = set()
count = 0
for x in res_list:
    if res_list.count(x) > 1:
        pass
    else:
        result.add(x)

print(len(result)) if len(result) > 0 else print("Таких нет")
 """


# 3_2_D

""" porridge_1_count, porridge_2_porridge_1_count, porridge_2_count = int(input()), int(input())

set_1 = set()
set_2 = set()
for x in range(porridge_1_count):
    set_1.add(input())
for x in range(porridge_2_count):
    set_2.add(input())count = int(input()), int(input())

set_1 = set()
set_2 = set()
for x in range(porridge_1_count):
    set_1.add(input())
for x in range(porridge_2_count):
    set_2.add(input())

set_3 = set_1 & set_2
if len(set_3) == 0:
    print("Таких нет")
else:
    print(len(set_3)) """


# 3_2_C

""" num = int(input())

area = set()
for x in range(num):
    area.add(input())

res_str = " ".join(area)
res_list = res_str.split(" ")
res_set = set(res_list)

for x in res_set:
    print(x)
 """



# 3_2_B

""" str_1, str_2 = set(input()), set(input())
print("".join(str_1 & str_2))
 """
# 3_2_A

""" print("".join(set(input())))
 """