##백준_2839

N=int(input())
'''
dp=[-1]*(N+1)
dp[0]=0


for i in range(1,N+1):
    if i<3:
        continue
    if i==3 or i==5:
        dp[i]=1
        continue
    if i<5:
        if dp[i-3]!=-1:
            dp[i]=dp[i-3]+dp[3]
    else:
        if dp[i-5]!=-1:
            dp[i]=dp[i-5]+dp[5]
        if dp[i]==-1:
            if dp[i-3]!=-1:
                dp[i]=dp[i-3]+dp[3]

print(dp[N])
'''
bag=0
while N>=0:
    if N%5==0:
        bag+=(N//5)
        print(bag)
        break
    N-=3
    bag+=1
else:
    print(-1)
