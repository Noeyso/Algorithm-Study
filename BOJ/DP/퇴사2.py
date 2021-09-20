N=int(input())

T,P=[],[]
dp=[0]*(N+1)

for i in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

for i in range(N):
    if T[i]<=N-i:
        dp[i+T[i]] = max(dp[i+T[i]],dp[i]+P[i])
    dp[i+1]=max(dp[i+1],dp[i])
    print(dp)


print(dp[N])

