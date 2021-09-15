##백준_11053 : 가장 긴 증가하는 수열(DP)

from sys import stdin
input = stdin.readline

N = int(input())
seq =list(map(int,input().split()))
dp=[0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if seq[i]>seq[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1


print(max(dp))
