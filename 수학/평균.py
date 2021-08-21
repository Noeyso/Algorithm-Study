N = int(input())

score=list(map(int,input().split()))

max_score = max(score)

total=[]
for i in score:
    total.append(i/max_score*100)

print(sum(total)/N)
