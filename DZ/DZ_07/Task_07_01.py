# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os

root = os.path.join(os.curdir, 'my_project')

my_pr_list = ['settings','mainapp','adminapp','authapp']

for el in my_pr_list:
    os.makedirs(os.path.join(root,el),exist_ok=True)
