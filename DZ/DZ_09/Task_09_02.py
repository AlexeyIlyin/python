class Road:
    _length = 5000
    _width = 10

    def massa_pol (self, expenditure, thickness):
        massa = Road._length * Road._width * expenditure * thickness
        return massa

r = Road()
print(f'Масса полотна {r.massa_pol(25,5)/1000} тонн')
