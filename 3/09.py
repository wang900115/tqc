num = int(input())
n = float(input())
m = int(input())
print("%s \t %s"%('Month','Amount'))
for i in range(1,m+1):
    num+=num*n/1200
    print("%3d \t %.2f"%(i,num))
