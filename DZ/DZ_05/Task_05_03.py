from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Михаил', 'Геннадий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


# #v1
# tut_g = ((tutor,klass) for tutor, klass in zip(tutors, klasses))
# print(*tut_g)
# print(*tut_g)

#v2
tut_g = ((tutor,klass) for tutor, klass in zip_longest(tutors, klasses, fillvalue=None))
print(*tut_g)
print(*tut_g)