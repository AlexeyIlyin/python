numbers = range (1,101)
for i in numbers:
    if (i >= 11) and (i <= 14):
        print (i, 'процентов')
    elif i % 10 == 1:
        print(i, 'процент')
    elif (i % 10 > 1) and (i % 10 <= 4):
        print(i, 'процента')
    elif ((i % 10 > 4) and (i % 10 <= 9)) or (i % 10 == 0):
        print(i, 'процентов')


