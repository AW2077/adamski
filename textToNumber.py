from tkinter import N


def text_to_number_eng(text):
    num = 0
    for i, letter in enumerate(text):
        num = num + ord(letter) * (128**i)
    return num

def text_to_number_pl(text):
    num = 0
    for i, letter in enumerate(text):
        num = num + ord(letter) * (381**i)
    return num

def number_to_text_eng(num):
    text = ''
    while num > 0:
        r = num % 256
        text += chr(r)
        num -= r
        num = num // 256
    reversed(text)
    return text

print(text_to_number_eng("pineapple"))
print(text_to_number_pl("słowo"))
print(number_to_text_eng(80))
