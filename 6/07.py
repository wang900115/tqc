n = ["1st","2nd","3rd"]
t = [[0 for j in range(5)] for i in range(3)]
for i in range(3):
    print("The {} student:".format(n[i]))
    for j in range(5):
        t[i][j]=int(input())
    
for i in range(3):
    print("Student %d"%(i+1))
    print("#Sum %d"%(sum(t[i])))
    print("#Average %.2f"%(sum(t[i])/5))
    
