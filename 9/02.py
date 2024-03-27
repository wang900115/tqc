f=open('read.txt')
w = f.read()
sp = w.split()
total = 0
for i in sp:
    total+=int(i)
print(total)
f.close()