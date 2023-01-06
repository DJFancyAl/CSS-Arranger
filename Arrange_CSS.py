import re

file = input('File Location: ')
file = file.replace("\\", "/").strip("\"")

with open(file) as reader:
    data = reader.read()
    styles = re.findall("([^}]+)", data)

for index, value in enumerate(styles):
    styles[index] = value.strip() + '\n}'

newList = sorted(styles)
newStyles = ""
for style in newList:
    newStyles += style + "\n\n"

with open(file, 'w') as reader:
    reader.write(newStyles)

print('Completed')

input()