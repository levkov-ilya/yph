new_list = []

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