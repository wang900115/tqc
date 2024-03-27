x1 = eval(input())
x2 = eval(input())
y1 = eval(input())
y2 = eval(input())
s = ((x1-x2)**2+(y1-y2)**2)**0.5
print(f"( {x1} , {x2} )")
print(f"( {y1} , {y2} )")
print("Distance: %.4f"%s)