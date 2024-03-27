n = []
for i in range(9):
    n.append(int(input()))

m = max(n)
mi = n.index(m)
print("Index of the largest number {} is : ({}, {})".format(m,mi//3,mi%3))

s = min(n)
si = n.index(s)
print("Index of the smallest number {} is : ({}, {})".format(s,si//3,si%3))

