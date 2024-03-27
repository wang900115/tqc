a = int(input())
b = int(input())
count = 0
result = 0
for i in range(a,b+1):
    if i%4 == 0 or i%9==0:
        result+=i
        print(i,end=' ')
        count+=1
        if count%10==0:
            print()
print()
print(count)
print(result)
