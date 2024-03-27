color_dict = dict()
key = input('Key:')
while key != 'end':
    value = input('Value')
    color_dict[key]=value
    key = input('Key:')

for i in sorted(color_dict.keys()):
    print(i+': '+color_dict[i])