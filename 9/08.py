f_name = input()
count = int(input())
freq = {}
f = open(f_name,'r')
w = f.read()
sp1 = w.split()
setsp1 = sorted(set(sp1))
for i in setsp1:
    if count == sp1.count(i):
        print(i)