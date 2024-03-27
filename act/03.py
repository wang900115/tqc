def compute(num):
    if num>100 or num<0:
        return -1
    elif num >= 60:
        num+=5
    else:
        num+=10
    return num
print(compute(int(input())))