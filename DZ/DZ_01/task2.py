numbers = range (1, 1000, 2)
# print(list(numbers))
summa=0
summa17=0
kube = []

for i in range (len(numbers)):
    kube.append(str(numbers[i]**3))    # строим список нечетных чисел в кубе, сразу переводим в строку
    kube_summ = 0

# считаем первую сумму
    for s in kube [i]:    # ищем сумму цифр
        kube_summ = kube_summ + int(s)
    if kube_summ % 7 == 0:    # проверяем на кратность 7
        summa = summa + int(kube[i])    # если кратно 7, суммируем

# считаем вторую сумму
    kube_summ = 0    # обнуляем сумму цифр от результата предыдущего цикла
    value17 = int(kube[i]) + 17    # присваиваем временной переменной значение элемента + 17
    for s in str(value17):    # увеличиваем на 17 и опять ищем сумму цифр
        kube_summ = kube_summ + int(s)
        if kube_summ % 7 == 0:  # проверяем на кратность 7
            summa17 = summa17 + value17  # если кратно 7, суммируем

print ('Сумма чисел в 3-й степени кратных 7 равна ', summa)
print ('Сумма чисел в 3-й степени кратных 7 и увеличенных на 17 и кратных 7 равна ', summa17)



