a = int(input())
if(a==0):
    print(a)
else:
    while a>0:
        print(a%10,end='')
        a=a//10