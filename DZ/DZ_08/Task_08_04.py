def val_checker (val_x):
    def _val_checker (funk):
        def wrapper (args):

            if val_x(args):
                result = funk(args)
                return print (result)
            else:
                print (f'ValueError: wrong val {args}')

        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

el = int(input('Введите число: '))
calc_cube(el)