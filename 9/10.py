M = 0 
F = 0
f = open('read.dat','r',encoding='utf-8')
w = f.readlines()
for i in w:
    print(i)
    sp = i.split()
    if sp[2]=='1':
        M+=1
    elif sp[2]=='0':
        F+=1
print("Number of males:{}".format(M))
print("Number of females:{}".format(F))