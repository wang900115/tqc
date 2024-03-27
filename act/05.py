string = input()
result = int(string[-1])
for char in string[:-1]:
    result *= int(char)
    print(f'{char}',end='*')
print(f"{string[-1]}={result}")