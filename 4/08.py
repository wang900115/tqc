odd = 0
even = 0
for _ in range(10):
    num = int(input())
    if num % 2:
        odd+=1
    else:
        even+=1
print(f'Even number: {even}')
print(f'Odd number: {odd}')