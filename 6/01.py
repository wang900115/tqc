n = []
count=result = 0
for _ in range(12):
    num = int(input())
    n.append(num)
for num in n:
    print(f"{num:>3d}",end = ' ')
    count+=1
    if count %3==0:
        print()
    result+=num
print(result)