lang = input('Выберите язык (EN/RU): ').upper()
cipher = []
ALPHABET_EN = 'abcdefghijklmnopqrstuwxyz'
ALPHABET_RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
if lang == 'RU':
    alphabet = ALPHABET_RU
elif lang == 'EN':
    alphabet = ALPHABET_EN
else:
    print('Проверьте корректность введенного вами языка')
    exit()
message = input('Введите сообщение: ').lower()
step = int(input('Введите шаг сдвига: '))
for letter in message:
    index = alphabet.find(letter) + step
    cipher.append(index)
print(cipher)
result = '' 
for number in cipher:
    result += alphabet[number - step] 
print(result)



