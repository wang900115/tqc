def compute(a,b,c):
    if b**2-4*a*c > 0:
        result1 = (-b+(b**2-4*a*c)**0.5)/(2*a) 
        result2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
        return f'{result1:.1f}, {result2:.1f}'
    elif b**2-4*a*c == 0:
        result = -b/(2*a)
        return f'{result:.1f}'
    else:
        return 'Your equation has no root'

a = int(input())
b = int(input())
c = int(input())

print(compute(a,b,c))