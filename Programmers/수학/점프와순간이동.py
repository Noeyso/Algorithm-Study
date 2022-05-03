##효율성에서 탈락
def solution(n):
    ans = 0
    dp=[i for i in range(n+1)]
    
    for i in range(1,n+1):
        dp[i]=min(dp[i-1]+1,dp[i])
        if i*2<=n:
            dp[i*2]=min(dp[i*2],dp[i])
    return dp[n]

##솔루션
def solution(n):
    ans = 0
    dp=[i for i in range(n+1)]
    
    for i in range(1,n+1):
        dp[i]=min(dp[i-1]+1,dp[i])
        if i*2<=n:
            dp[i*2]=min(dp[i*2],dp[i])
    return dp[n]
