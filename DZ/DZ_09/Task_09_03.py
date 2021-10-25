class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.postion = position
        self._income = {'wage' : wage, 'bonus': bonus}


class Postion(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        self.full_name = ' '.join ([self.name, self.surname])
        return self.full_name

    def get_total_income (self):
        self.total_income = self._income['wage'] + self._income['bonus']
        return self.total_income


w1 = Postion ('Иванов', 'Иван', 'Мастер', 100000, 20000)
w2 = Postion ('Петров', 'Петр', 'Слесарь', 80000, 10000)



print (w1.get_full_name(), w1.get_total_income())
print (w2.get_full_name(), w2.get_total_income())