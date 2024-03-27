# for i in range(int(input())):
#     n = str(input())
#     a = [int(j) for j in n]
#     print("Sum of all digits of "+str(n)+" is "+str(sum(a)))

# a = int(input())
# for i in range(a):
#     ans = 0
#     n = str(input())
#     for i in range(0,len(n)):
#         ans+=int(n[i])
#     print("Sum of all digits of "+str(n)+" is "+str(ans))

n = eval(input())
for i in range(n):
    num = eval(input())
    t = num
    ans = 0
    while t !=0 :
        ans += t%10
        t //= 10
    print("Sum of all digits of ",num,"is",ans)

