LIST = []
num = eval(input())
while num!=-9999:
    LIST.append(num)
    num = eval(input())
LIST = tuple(LIST)
print(LIST)
print("Length:",len(LIST))
print("Max:",max(LIST))
print("Min:",min(LIST))
print("Sum:",sum(LIST))