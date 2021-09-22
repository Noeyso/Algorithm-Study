##백준_12026 : BOJ 거리 (DP)
from sys import stdin
input = stdin.readline

N = int(input())
road = list(input().rstrip())

MAX=999999999
dp=[MAX]*N

def get_prev(x):
    if x=="B":
        return "J"
    elif x=="O":
        return "B"
    elif x=="J":
        return "O"
    
dp[0]=0

for i in range(1,N):
    prev = get_prev(road[i])
    for j in range(i):
        if road[j]==prev:
            dp[i]=min(dp[i],dp[j]+pow(i-j,2))
            
print(dp[N-1] if dp[N-1]!=MAX else -1)
