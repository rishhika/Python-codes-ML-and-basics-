fname = input('Enter the file name:')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened', fname)
    quit()
c = 0
for line in fhandle:
    c =c + 1
    print(c, line)
