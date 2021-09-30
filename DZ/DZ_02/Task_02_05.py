prices = [57.8, 46.51, 97, 56.38, 75.6, 15.8]

for i in range(len(prices)):
    r = int(prices[i] // 1)    # вычисляем рубли
    k = int (round((prices[i] % 1) * 100, 1))    # вычисляем копейки
    print(r, 'руб.', k, 'коп.')    # печатаем в требуемом формате