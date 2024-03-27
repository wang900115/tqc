
dict1 = {}
print('Create dict1:')
key = input('Key:')
while key != 'end':
    value = input('Value:')
    dict1[key]=value
    key = input('Key:')


dict2 = {}
print('Create dict2:')
key = input('Key:')
while key != 'end':
    value = input('Value:')
    dict2[key]=value
    key = input('Key:')

dict1.update(dict2)
for i in sorted(dict1.keys()):
    print(i+': '+dict1[i])


