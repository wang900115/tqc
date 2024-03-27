import math
def compute(p,q):
    common = math.gcd(p,q)
    return common

x,y = eval(input())
m,n = eval(input())

q = y*n
p = m*y+x*n
gcd = compute(q,p)
print(f"{x}/{y} + {m}/{n} = {int(p/gcd)}/{int(q/gcd)}")