##백준_1141

N = int(input())
words=[input() for _ in range(N)]
words.sort(key=len)

ans=0
for i in range(N):
    word = words[i]
    isHead==False
    for j in range(i+1,N):
        try:
            if words[j].index(word)==0:
                isHead=True
                break
        except:
            continue
    if not isHead:
        ans+=1
print(ans)

