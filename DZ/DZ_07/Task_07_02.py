# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html

import os
import shutil

with open('config.yaml', 'r', encoding='utf-8') as f:
    lines = dict(map(str.split, f.readlines()))


root = lines.pop('root')

for k, v in lines.items():
    os.makedirs(os.path.join(os.curdir, root, k), exist_ok=True)
    print(f'Создан каталог:{k}')
    for i in v.split(','):
        with open (os.path.join(os.curdir, root, k, i), 'w', encoding='utf-8'):
            print(f'Создан файл: {i} в каталоге {k}')
