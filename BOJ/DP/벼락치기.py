##백준_14728 : 벼락치기 (배낭문제)

N,T = map(int,input().split())
arr=[[0,0]]
dp=[[0]*(T+1) for _ in range(N+1)]
for _ in range(N):
    arr.append(list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,T+1):
        time=arr[i][0]
        score=arr[i][1]

        if j<time:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(score+dp[i-1][j-time],dp[i-1][j])
print(dp[N][T])
