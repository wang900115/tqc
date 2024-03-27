n = []
for _ in range(10):
    num = int(input())
    n.append(num)
freq = {}

for num in n:
    freq[num]=freq.get(num,0)+1

print(max(freq.items(),key = lambda x:x[1])[0])
print(max(freq.items(),key = lambda x:x[1])[1])