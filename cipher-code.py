print('Hello, I will help you to encrypt or decrypt your text')
print('Now, ask the question what do you need? - encryption / decryption')
answer = input().lower()
print('What language do you need? - ru / en')
lang = input().lower()
print('Step shift?')
step = int(input())


alpha_ru = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alpha_lower_ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alpha_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lower_en = "abcdefghijklmnopqrstuvwxyz"


print('Your message:')
message = input()

def cipher(strr, step):
    result = ''
    if lang == 'ru':
        for char in strr:
            if char.isalpha():  
                if char.isupper():
                    ind = alpha_ru.find(char)
                    number = (ind + step) % 32  
                    result += alpha_ru[number]
                else:
                    ind = alpha_lower_ru.find(char)
                    number = (ind + step) % 32
                    result += alpha_lower_ru[number]
            else:
                result += char  

    elif lang == 'en':
        for char in strr:
            if char.isalpha():
                if char.isupper():
                    ind = alpha_en.find(char)
                    number = (ind + step) % 26
                    result += alpha_en[number]
                else:
                    ind = alpha_lower_en.find(char)
                    number = (ind + step) % 26
                    result += alpha_lower_en[number]
            else:
                result += char  

    print('Result:', result)

if answer == 'encryption':
    cipher(message, step)
elif answer == 'decryption':
    cipher(message, -step)
else:
    print("Invalid option. Please choose 'encryption' or 'decryption'.")
