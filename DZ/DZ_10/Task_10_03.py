class Cell:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        res = self.x + other.x
        return  str(res)

    def __sub__(self, other):
        res = self.x - other.x
        if res <= 0:
            res = ('Разность клеток равна 0 или отрицательная')
        return  str(res)

    def __mul__(self, other):
        res = self.x * other.x
        return  str(res)

    def __floordiv__(self, other):
        res = self.x // other.x
        return  str(res)

    def make_order(self,cl,k):
        res = ''
        for i in range(self.x):
            if i % k == 0:
                res += '\n'
            res += '*'
        return res

a = Cell(int(input('Введите значение первой клетки: ')))
b = Cell(int(input('Введите значение второй клетки: ')))

print('Результат сложения клеток: ', a + b)
print('Результат вычитания клеток: ', a - b)
print('Результат умножения клеток: ', a * b)
print('Результат деления клеток: ', a // b)

print (a.make_order(a,5))