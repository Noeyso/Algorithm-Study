## 백준_1059

L = int(input())
S = sorted(list(map(int,input().split())))
n = int(input())

start,end = 1,0

if n in S:
    print(0)
else:
    for i in S:
        if i<n:
            start=i+1
        else:
            end=i-1
            break
    print(start,end)
    print(end-start+(n-start)*(end-n))
