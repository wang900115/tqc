s = input()
a = ''
b = ''
for char in s:
    if char.isupper():
        a+=char
    else:
        b+=char

print(a)
print(b)
print(len(a))
    