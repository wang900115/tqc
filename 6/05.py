scores=[0]*10
for i in range(10):
    scores[i] = int(input())
scores.sort()
print(sum(scores[1:-1]))
print(f"{sum(scores[1:-1])/8:.2f}")