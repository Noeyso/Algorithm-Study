##백준_15989 : 1,2,3더하기 4

T=int(input())
MAX=10**4
dp = [[0]*(MAX+1) for _ in range(4)]

for _ in range(T):
    num = int(input())
    for i in range(1,4):
        dp[i][0]=1
        for j in range(1,num+1):
            if dp[i][j]!=0:
                continue
            dp[i][j]=dp[i-1][j]+dp[i][j-i]
    print(dp[3][num])
