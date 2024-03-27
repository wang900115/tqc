l = [0]*10
for i in range(10):
    l[i]= int(input())
l.sort()
print(l[-1],l[-2],l[-3])