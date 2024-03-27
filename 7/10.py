p = dict()
key = input('Key:')
while key != 'end':
    value = input('Value:')
    p[key]=value
    key = input('Key:')
Search_key=input('Search key:')
print(Search_key in p)