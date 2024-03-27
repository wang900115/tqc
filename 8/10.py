k = int(input())
for i in range(k):
    n = list(map(float,input().split()))
    print("{:.2f}".format(max(n)-min(n)))