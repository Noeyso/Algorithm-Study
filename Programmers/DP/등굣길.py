from collections import deque

def solution(m, n, puddles):
    dp=[[0]*m for _ in range(n)]
    que=deque([])
    que.append((0,0))
    dp[0][0]=1
    for x,y in puddles:
        dp[y-1][x-1]=-1

    while que:
        y,x =que.popleft()
        moves=[(y+1,x),(y,x+1)]
        for my,mx in moves:
            if mx<m and my<n and dp[my][mx]!=-1:
                if dp[my][mx]==0:
                    que.append((my,mx))
                dp[my][mx]+=dp[y][x]
    return dp[n-1][m-1]%(1000000007)

print(solution(4,3,[[2,2]]))
