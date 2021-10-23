def num_translate (eng_num):
    numbers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if eng_num[0].islower():
        return numbers.get(eng_num, 'ошибка')
    elif eng_num[0].istitle():
#        return numbers [eng_num.lower()].title()
        return numbers.get(eng_num.lower(), 'ошибка').title()

val = input('Введите число от 1 до 10 на английском: ')

print(num_translate(val))