##백준_2294

N,K = map(int,input().split())
dp=[10001 for _ in range(K+1)]
dp[0]=0
for i in range(N):
    c = int(input())
    for j in range(c,K+1):
        dp[j]=min(dp[j],dp[j-c]+1)

dp[-1]=dp[-1] if dp[-1]!=10001 else -1
print(dp[-1])
