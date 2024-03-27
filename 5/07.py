def compute(x):
    for i in range(2,x):
        if x%i == 0:
            return 'Not Prime'
    return 'Prime'

x = int(input())
print(compute(x))
