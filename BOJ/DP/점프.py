## 백준_1890

from sys import stdin

input=stdin.readline

N = int(input())
board=[]
for i in range(N):
    board.append(list(map(int,input().split())))

dp=[[0]*N for _ in range(N)]
dp[0][0]=1

for i in range(N):
    for j in range(N):
        if i==N-1 and j==N-1:
            print(dp[i][j])
            break
        num=board[i][j]
        if j+num<N:
            dp[i][j+num]+=dp[i][j]
        if i+num<N:
            dp[i+num][j]+=dp[i][j]
