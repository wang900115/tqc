n = input()
result = 0
for i in range(len(n)):
    print('ASCII code for \''+n[i]+'\':'+str(ord(n[i])))
    result+=ord(n[i])
print(result)