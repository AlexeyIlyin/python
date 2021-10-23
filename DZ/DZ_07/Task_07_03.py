import os
import shutil

new_templ_dir = r'my_project2\templates'
for root, dirs, files in os.walk ('my_project2'):
    if root == new_templ_dir:
        break
    for file in files:
        if file.rsplit('.', 1)[-1].lower() == 'html':
            os.makedirs(os.path.join(new_templ_dir, root.rsplit('\\',1)[-1]), exist_ok=True)
            shutil.copyfile(os.path.join(root, file), os.path.join(new_templ_dir, os.path.join(root.rsplit('\\',1)[-1],file)))
    # print('root: ', root, 'dirs: ', dirs,'files: ', files)