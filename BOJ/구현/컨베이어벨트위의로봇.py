from sys import stdin
from collections import deque

input = stdin.readline
N,K = map(int,input().split())
belt = deque(map(int,input().split()))
step=1
robots=deque([0]*N)
while True:
    ## 1. 벨트를 움직인다.
    belt.rotate(1)
    robots.rotate(1)
    robots[-1]=0
    
    ## 2. 벨트에 로봇이 있다면 한칸 이동
    for i in range(N-2,-1,-1):
        if robots[i]!=0 and robots[i+1]==0 and belt[i+1]>0:
            belt[i+1]-=1
            robots[i+1]=robots[i]
            robots[i]=0
    robots[-1]=0
    
    ## 3. 내구도가 0보다 크고 자리에 다른 로봇이 없으면 => 로봇 올리기
    if belt[0]>0 and robots[0]==0:
        belt[0]-=1
        robots[0]=1

    ## 4. 내구도 0이 K이상이면 종료
    count=0
    for i in range(2*N):
        if belt[i]==0:
            count+=1

    if count>=K:
        print(step)
        break
    step+=1
