## 백준_2293 : 동전 1
from sys import stdin

N,K=map(int,stdin.readline().split())
coin=[int(stdin.readline())for i in range(N)]
dp=[0 for i in range(K+1)]
dp[0]=1

for c in coin:
    for i in range(c,K+1):
      if i-c>=0:
          dp[i]+=dp[i-c]
print(dp[K])
