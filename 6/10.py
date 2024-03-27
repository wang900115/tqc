L = []
for w in range(1,5):
    print('Week %d:'%w)
    for D in range(1,4):
        x=eval(input('Day %d:'%D))
        L.append(x)
A = sum(L)/len(L)
print("Average: %.2F"%A)
print('Heighest:',max(L))
print('Lowest:',min(L))
