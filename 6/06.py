rows=int(input())
cols=int(input())

def compute(rows,cols):
    for i in range(rows):
        for j in range(cols):
            print(f"{j-i:4d}",end='')
        print()

compute(rows,cols)