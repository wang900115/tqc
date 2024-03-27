# def compute(num):
#     if num > 1:
#         return compute(num-1) + compute(num-2)
#     return num

# n = int(input())
# for i in range(n):
#     print(compute(i),end=' ')

def compute(n):
    curr = 1 
    pre = 0
    print(0,1,end=' ')
    for i in range(2,n):
        temp = curr + pre
        print(temp,end=' ')
        pre = curr 
        curr = temp

num = eval(input())
compute(num)
