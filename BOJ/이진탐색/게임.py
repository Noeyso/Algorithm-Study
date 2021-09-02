## 백준_1072

import sys
input = sys.stdin.readline

X,Y = map(int,input().rsplit())

s,e=1,X
victory=Y*100//X
ans=sys.maxsize

while s<=e:
    mid = (s+e)//2
    tmp = (Y+mid)*100//(X+mid)
    if tmp>victory:
        ans=min(mid,ans)
        e=mid-1
    else:
        s=mid+1

if ans==sys.maxsize:
    print(-1)
else:
    print(ans)
