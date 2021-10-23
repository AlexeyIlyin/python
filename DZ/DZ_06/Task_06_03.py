from itertools import zip_longest
import json

with open ('users.csv', 'r', encoding='utf-8') as f:
    users = f.readlines()
    users = list(map(lambda x: x.replace('\n', ' ').replace('\r', ' '), users))

with open ('hobby.csv', 'r', encoding='utf-8') as f:
    hobby = f.readlines()
    hobby = list(map(lambda x: x.replace('\n', ' ').replace('\r', ' '), hobby))

print(users)
print(hobby)

user_hobby = dict(zip_longest(users,hobby,fillvalue=None))
print(user_hobby)

# проверка
# user_hobby_str = json.dumps(user_hobby)
# print(type (user_hobby_str), user_hobby_str)
#
# us = json.loads(user_hobby_str)
# print(type(us), us)


with open ('user_hobby.json', 'w', encoding='utf-8') as f:
    json.dump(user_hobby, f)

