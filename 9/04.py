height = []
weight = []

maxh = 0
maxw = 0

f = open('read.txt','r')
w = f.readlines()

for x in w:
    print(x)
    ss = x.split()
    height.append(eval(ss[1]))
    weight.append(eval(ss[2]))

    if eval(ss[1])>maxh:
        maxh = eval(ss[1])
        hname = ss[0]
    
    if eval(ss[2])>maxw:
        maxw = eval(ss[2])
        wname = ss[0]
print('Average height: %.2f'%(sum(height)/len(height)))
print('Average weight: %.2f'%(sum(weight)/len(weight)))

print('The tallest is %s with: %.2f'%(hname,max(height)))
print('The heaviest is %s with: %.2f'%(wname,max(weight)))

f.close()