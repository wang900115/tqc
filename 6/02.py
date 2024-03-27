result = 0

for _ in range(5):
    num = input()

    if num.upper() == 'A':
        result+=1
    elif num.upper() == 'J':
        result+=11
    elif num.upper() == 'O':
        result+=12
    elif num.upper()== 'K':
        result+=13
    else:
        result+=int(num)

print(result)