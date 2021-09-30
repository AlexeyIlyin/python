dyration = int(input('Введите число: '))
days = dyration // (24 * 60 * 60)    # вычисляем целое число дней

hours = (dyration // (60 * 60)) - days * 24    # вычисляем целое число часов
min = (dyration // 60) - ( days * 24 * 60 + hours * 60)     # вычисляем целое число минут
sec = dyration % 60    # вычисляем целое число секунд

if days != 0 and hours != 0 and min != 0:
    print(days, 'дн', hours, ' час ', min, ' мин', sec, ' сек')
elif hours != 0 and min != 0:
    print(hours, ' час ', min, ' мин', sec, ' сек')
elif min != 0:
    print(min, ' мин', sec, ' сек')
else:
    print(sec, ' сек')

print('end')