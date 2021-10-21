def type_logger (funk):
    def wrapper (*args):
        for i in args:
           print (f'{i} : {type(i)}')
           print(funk(i), type(funk(i)))
    return wrapper


@type_logger
def calc_cube(x):
   return x ** 3

calc_cube(9,5,6)