a = int(input())

if a%3 == 0 and a%5!=0:
    print(f"{a} is a multiple of 3")
elif a%3 != 0 and a%5 == 0:
    print(f"{a} is a multiple of 5")
elif a%3 == 0 and a%5 == 0:
    print(f"{a} is a multiple of 3 and 5")
else:
    print(f"{a} is not a multiple of 3 or 5")
