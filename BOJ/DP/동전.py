##백준_9084 : 동전 (배낭문제)

T=int(input())

for i in range(T):
    N = int(input())
    coins=[0]
    coins+=list(map(int,input().split()))
    M = int(input())

    dp=[[0]*(M+1) for _ in range(N+1)]
    
    for n in range(1,N+1):
        dp[n][0]=1
        for m in range(1,M+1):
            coin=coins[n]
            if m<coin:
                dp[n][m]=dp[n-1][m]
            else:
                dp[n][m]=dp[n][m-coin]+dp[n-1][m]
                 
    print(dp[N][M])
