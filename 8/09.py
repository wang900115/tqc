n = input()
l1 = False
l2 = False
l3 = False
if len(n)>=0:
    l1=True
for char in n:
    if char.isalpha() or char.isdigit():
        l2=True
    if char.isupper():
        l3=True

if l1 and l2 and l3:
    print('Valod password')
else:
    print('Invalid password')
