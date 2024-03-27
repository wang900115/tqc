a = int(input())
b = int(input())
op = input()
if op == '+':
    result = a+b
elif op=="-":
    result = a-b
elif op=="*":
    result = a*b
elif op=="/":
    result = a/b
elif op=="//":
    result = a//b
else:
    result = a%b
print(result)