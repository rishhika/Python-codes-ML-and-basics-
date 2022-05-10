fhand = open('m-box.txt')
for line in fhand:
    if line.startswith('jbf '):
        print(line)
    if not line.startswith('jbf '):
        continue
print('END')