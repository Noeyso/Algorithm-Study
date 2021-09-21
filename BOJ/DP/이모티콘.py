from collections import deque

S = int(input())
dp=[[-1]*(S+1) for _ in range(S+1)]
q = deque()
q.append((1,0)) ## 이모티콘 개수, 클립보드 이모티콘 개수
dp[1][0]=0

while q:
    s,c = q.popleft()
    if dp[s][s]==-1:
        dp[s][s]=dp[s][c]+1
        q.append((s,s))
    if s+c<=S and dp[s+c][c]==-1:
        dp[s+c][c]=dp[s][c]+1
        q.append((s+c,c))
    if s-1>=0 and dp[s-1][c]==-1:
        dp[s-1][c]=dp[s][c]+1
        q.append((s-1,c))
        
answer=-1
for i in range(S+1):
    if dp[S][i]!=-1:
        if answer==-1 or answer>dp[S][i]:
            answer=dp[S][i]
        
print(answer)    
