## 백준_1268

N=int(input())

classes=[list(map(int,input().split())) for _ in range(N)]
count_s = [0]*N

for n in range(N):
    visited = [False for _ in range(N)]

    for grade in range(5):
        for s in range(N):
            if s!=n and classes[s][grade]==classes[n][grade]:
                visited[s]=True
    count_s[n] = len(list(filter(lambda x:x,visited)))
print(count_s.index(max(count_s))+1)
