## 백준_1965

N=int(input())
box=list(map(int,input().split()))
res=[1]*N

idx=0
for idx in range(N):
    m=0
    for i in range(0,idx):
        if box[i]<box[idx] and res[i]>m:
            m=res[i]
    res[idx]+=m

print(max(res))
