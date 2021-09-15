##백준_2565 : 전깃줄(DP)

from sys import stdin
input = stdin.readline

N = int(input())
arr= [list(map(int,input().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0])

arr_b=[]
dp=[0 for _ in range(N)]
for i in range(N):
    arr_b.append(arr[i][1])

for i in range(N):
    for j in range(i):
        if arr_b[i]>arr_b[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1

print(N-max(dp))
