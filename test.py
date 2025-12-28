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


        


# !!! 
ex_list = ["sample", "example"]
ex_tuple = ("1", "sample", "example")
ex_set = {"sample", "example"}
ex_dict = {"1": ("sample", "exmple"), "2": "example"}
ex_dict.update("test")
print(ex_dict)


""" print(type(ex_list))
print(type(ex_tuple))
print(type(ex_set))
print(type(ex_dict)) """

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
        print(x) """
# print(result)

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

def text_to_morse(text: str, morse_dict: dict) -> None:
    res_list = list(text.upper())
    res_list_morse = []
    for letter in res_list:
        for key in morse_dict: 
            if letter == key:
                res_list_morse.append(morse_dict[key])
    
    
    res_str = " ".join(res_list_morse)
    print(res_str.replace("  ", "\n"))
    print(res_str)
    print(res_list_morse)
    """
               
    # print(res_list)
    # print(res_list_morse)
    # print(f'{key} {morse_dict[key]}')
        


# print(text_to_morse("Help me SOS", MORSE_CODE_DICT))

""" text = "##sdfsf sdfsdf@@@"
print(text[:-3]) """

""" count = int(input())

print(f"А Б В")
for a in range(1, count):
    for b in range(1, count):
        for c in range(1, count):
            if a + b + c == count:
                print(f"{a} {b} {c}") """


""" num = 123782136

max_num = 0
x_ = 0
for x in str(num):
    if x >= max_num:
        max_num == x

print(x) """

""" res = {"Иванов", "Алмазов", "Жопов", "Янусов", "Яичкин"}
print(sorted(res)) """