def compute(a,y,x):
    for i in range(x):
        for j in range(y):
            print(a,end=' ')
        print()

a = input()
x = int(input())
y = int(input())
compute(a,x,y)