while True:
    hight = int(input())
    weight = int(input())
    if hight == -9999:
        break
    BMI = weight/((hight/100 )** 2)
    print('BMI:%.2F'%BMI)
    if BMI >= 30:
        print('State: fat')
    elif BMI >= 25:
        print('State: over weight')
    elif BMI >= 18.5:
        print('State: normal')
    else:
        print('State: under weight')