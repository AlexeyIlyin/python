import random

def rand_num (rnd_n):
    for i in range(1, rnd_n+1,2):
        print(f'Для {i} итерации случайное число {random.randint(1,int(i))}')
    return

n = int (input('Введите число: '))

rand_num(n)