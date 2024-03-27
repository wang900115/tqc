score = int(input())
if score>100 or score<0:
    print('error')
elif score > 60:
    score+=10
    print(score)
else:
    score+=5
    print(score)
