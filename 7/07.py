x = set()
y = set()



string = input('Enter group X\'s subjects:\n')
while string != 'end':
    x.add(string)
    string = input()

string = input('Enter group Y\'s subjects:\n')
while string != 'end':
    y.add(string)
    string = input()
print(sorted((x.union(y))))
print(sorted((x.intersection(y))))
print(sorted((y.difference(x))))
print(sorted((x.symmetric_difference(y))))
