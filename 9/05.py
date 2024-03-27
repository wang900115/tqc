file = input()
string = input()
with open(file,"r+",encoding='utf-8') as f:
    data = f.read()
    print('=== Before the deletion')
    print(data)
    print('=== After the deletion')
    data = data.replace(string,"")
    print(data)
    f.seek(0)
    f.write(data)
    