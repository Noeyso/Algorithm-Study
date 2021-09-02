##백준_2579 : 계단오르기

from sys import stdin

stair=[]
n=int(stdin.readline())
for i in range(n):
    stair.append(int(input().strip()))


dp=[]
dp.append(stair[0])
while True:
    if n==1:
        print(dp[0])
        break
    else:
        dp.append(stair[0]+stair[1])
        if n==2:
            print(dp[1])
            break
        dp.append(max(stair[0]+stair[2],stair[1]+stair[2]))
        if n==3:
            print(dp[2])
            break
        if n>2:
            for i in range(3,n):
                dp.append(max(stair[i]+stair[i-1]+dp[i-3],stair[i]+dp[i-2]))
        print(dp[-1])
        break
