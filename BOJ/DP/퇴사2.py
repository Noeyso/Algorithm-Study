##백준_15486

from sys import stdin
input = stdin.readline

N=int(input())

T,P=[],[]
dp=[0]*(N+1)

for i in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

m = 0
for i in range(N):
    m=max(m,dp[i])
    if T[i]<=N-i:
        dp[i+T[i]] = max(dp[i+T[i]],m+P[i])


print(max(dp))
