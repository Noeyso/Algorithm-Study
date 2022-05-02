def solution(sticker):
    N = len(sticker)
    if N==1:
        return sticker[0]
    dp=[0]*N
    dp2=[0]*N

    dp[0]=sticker[0]
    dp[1]=sticker[0]

    dp2[0]=0
    dp2[1]=sticker[1]

    for i in range(2,N-1):
        dp[i] = max(dp[i-2]+sticker[i],dp[i-1])
    sum_1 = max(dp)

    for i in range(2,N):
        dp2[i] = max(dp2[i-2]+sticker[i],dp2[i-1])
    sum_2 = max(dp2)

    return max(sum_1,sum_2)
