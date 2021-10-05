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
#    return numbers [eng_num]
    return numbers.get(eng_num, 'ошибка')

val = input('Введите число от 1 до 10 на английском: ')

print(num_translate(val))
