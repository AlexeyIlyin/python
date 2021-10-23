import os
import json

size_dict = {}
for root, dirs, files in os.walk('my_project2'):
    for file in files:
        key_dict = os.stat(os.path.join(root, file)).st_size//10*10+10
        f_ext = file.rsplit('.')[-1]
        if key_dict in size_dict:
            size_dict[key_dict][1].append(f_ext)
            size_dict[key_dict] = (size_dict[key_dict][0] + 1, list(set(size_dict[key_dict][1])))
        else:
            size_dict.setdefault(key_dict, (1, [f_ext]))

print(size_dict)

with open ('result.json', 'w') as f:
    json.dump(size_dict, f)

with open('result.json', 'r') as f:
    print(json.load(f))