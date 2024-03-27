s1 = input()
s2 = input()
n = int(input())
if n>len(s1):
    print('error')
elif s1[:n]>s2[:n]:
    print(f"{s1} > {s2}")
elif s1[:n]<s2[:n]:
    print(f"{s1} < {s2}")
else:
    print(f"{s1} = {s2}")