##백준_16953

from collections import deque

A,B = map(int,input().split())
res=-1
que = deque([(A,1)])

while que:
    i,cnt=que.popleft()
    if i==B:
        res=cnt
        break
    if i*2<=B:
        que.append((i*2,cnt+1))
    if i*10+1 <=B:
        que.append((i*10+1,cnt+1))
    
print(res)
