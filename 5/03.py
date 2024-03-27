def compute(a,b):
    result = 0
    for i in range(a,b+1):
        result += i
    return result

a = int(input())
b = int(input())
print(compute(a,b))