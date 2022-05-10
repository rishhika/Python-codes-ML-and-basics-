handle = open('m-box.txt', 'r')
print(handle)
fhand = open('m-box.txt')
c = 0
for x in fhand:
    c = c + 1
print("Line count:", c)
str = fhand.read()
//print(len(str))//
