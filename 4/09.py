number_1 = 0
number_2 = 0
number_else = 0

for _ in range(5):
    num = int(input())
    if num == 1:
        number_1 +=1
    elif num == 2:
        number_2 +=1
    else:
        number_else +=1
    print(f'Total votes of No.1:Nami = {number_1}')
    print(f'Total votes of No.2:Chopper = {number_2}')
    print(f'Total null votes = {number_else}')

if number_1 > number_2:
    print('=> No.1 Nami won the election')
elif number_1 < number_2:
    print('=> No.2 Chopper won the election')
else:
    print('=> No one won the election')