t = tuple()
string = input()
while string != 'end':
    t+=(string,)
    string = input()
print(t)
print(t[:3])
print(t[-3:])
