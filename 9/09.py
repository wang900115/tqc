with open('data.dat','w',encoding='utf-8') as fp:
    for i in range(5):
        fp.write(input()+'\n')
print('The content of \"data.dat\":')
with open('data.dat','r',encoding='utf-8') as fp:
    for i in fp:
        print(i)