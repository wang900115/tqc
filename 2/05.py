p = input()
if p.isalpha():
    print(f"{p} is an alphabet.")
elif p.isdigit():
    print(f"{p} is a number.")
else:
    print(f"{p} is a symbol.")