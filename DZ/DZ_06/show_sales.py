import sys

command = sys.argv

print(command, len(command))

with open('bakery.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    #print(lines[start:end])

if len(command) == 1:
    print(lines)
elif len(command) == 2:
    start = int(command[1])-1
    print(lines[start:])
else:
    start = int(command[1])-1
    end = int(command[2])
    print(lines[start:end])


