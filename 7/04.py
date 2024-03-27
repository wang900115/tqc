s = set()
while True:
    num = eval(input())
    if num == -9999:
        break
    s.add(num)
print("Length:",len(s))
print("Max:",max(s))
print("Min:",min(s))
print("Sum:",sum(s))