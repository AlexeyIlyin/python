# Родительский класс
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = color
        self. name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print ('Машина остановилась.')

    def turn(self,direction):
        print(f'Машина повернула {direction}')

    def show_speed (self, speed_now):
        print(f'Текущая скорость {speed_now} км/ч')

# дочерние классы
class TownCar (Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        return

    def show_speed(self, speed_now):
        limit = 60
        if speed_now > limit:
            print(f'Текущая скорость {speed_now} км/ч, превышение скорости на {speed_now-limit} км/ч')
        else:
            print(f'Текущая скорость {speed_now} км/ч')

class SportCar (Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        return

class WorkCar (Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        return

    def show_speed(self, speed_now):
        limit = 40
        if speed_now > limit:
            print(f'Текущая скорость {speed_now} км/ч, превышение скорости на {speed_now-limit} км/ч')
        else:
            print(f'Текущая скорость {speed_now} км/ч')
        return

class PoliceCar (Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police=True)
        return

# функция вывода инфо по автомобилю
def car_info (car):
    print(f'Автомобиль марки {car.name}, цвет {car.color}, максимальная скорость {car.speed} км/ч')

# создание объектов
car1 = TownCar(180, 'черный', 'Mersedes', False)
car2 = SportCar(250, 'красный', 'Ferrari', False)
car3 = WorkCar(90, 'серый', 'MAN', False)
car4 = PoliceCar(200, 'белый', 'Audi', True)

# вывод информации
car_info(car1)
car1.go()
car1.show_speed(20)
car1.show_speed(90)
car1.turn('направо')
car1.stop()

car_info(car2)
car2.go()
car2.show_speed(70)
car2.show_speed(120)
car2.turn('налево')
car2.stop()

car_info(car3)
car3.go()
car3.show_speed(55)
car3.show_speed(135)
car3.turn('направо')
car3.stop()

car_info(car4)
car2.go()
car2.show_speed(50)
car2.show_speed(168)
car2.turn('налево')
car2.stop()