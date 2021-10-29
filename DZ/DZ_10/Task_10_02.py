from abc import ABC, abstractmethod

class MyAbcClass(ABC):
    @abstractmethod
    def coat(self):
        pass
    @abstractmethod
    def suit(self):
        pass

class Clothes(MyAbcClass):
    def __init__(self, title):
        self.title = title

    def coat(self, v):
        result = v/6.5 + 0.5
        return result

    def suit(self, h):
        result = 2*h + 0.3
        return result

pal = Clothes('Пальто')
kos = Clothes('Костюм')
print(f'Расход на пошив {pal.title} составит {pal.coat(1.5)} м.')
print(f'Расход на пошив {kos.title} составит {kos.suit(1)} м')