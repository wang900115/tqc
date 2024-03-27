# import math
# def compute(x,y):
#     return math.gcd(x,y)

# x,y = map(int,input().split(','))
# print(compute(x,y))

def compute(x,y):
    while y!=0:
        temp = y 
        y = x%y
        x = temp
    print(x)

x,y =eval(input())
compute(x,y)