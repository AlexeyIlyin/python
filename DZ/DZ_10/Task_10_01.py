from itertools import zip_longest

class Matrix:
    def __init__(self, mt):
        self.mt = mt

    def __str__(self):
        for row in self.mt:
            print(' '.join(map(str,row)))
        return ''

    def __add__(self, other):
        mt_res = ''
        x = max(len(self.mt), len(other.mt))
        y = max(len(self.mt[0]), len(other.mt[0]))

        # print(x,y)
        # for i in range(x):     #len(self.mt)):
        #     for j in range(y):     #len(self.mt[i])):
        #         try:
        #             print(self.mt[i][j] + other.mt[i][j])
        #         except IndexError:
        #             print('0' if other.mt[i][j] is None else other.mt[i][j])
        #         except IndexError:
        #             print('0' if self.mt[i][j] is None else self.mt[i][j])
        #         # mt_res[i][j] = self.mt[i][j] + other.mt[i][j]
        #
        # return mt_res

        # for i in range(x):
        #     tp = zip_longest(self.mt[i], other.mt[i], fillvalue=0)
        #     print(*tp)

        for m1, m2 in zip_longest(self.mt, other.mt,fillvalue=[0]):
            for el1, el2 in zip_longest(m1, m2, fillvalue=0):
                mt_res += str(el1+el2)+' '
            mt_res += '\n'

        return mt_res




mt1 = Matrix([[31, 22], [37, 43], [51, 86]])
mt2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
mt3 = Matrix([[3,5,8,3],[8,3,7,1]])
mt4 = Matrix([[3, 5], [2, 4], [-1, 64]])

# print(mt1)
# print(mt2)
# print(mt3)

print(mt1 + mt2)
print(mt1 + mt3)
print(mt2 + mt3)