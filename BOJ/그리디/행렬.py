## 백준_1080

from sys import stdin

input=stdin.readline

N,M = map(int,input().split())
cnt=0

A=[list(map(int,input().rstrip())) for _ in range(N)]
B=[list(map(int,input().rstrip())) for _ in range(N)]

def convert(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            A[i][j]=1-A[i][j]

def check():
    for i in range(N):
        for j in range(M):
            if A[i][j]!=B[i][j]:
                return False
    return True
    

for i in range(N-2):
    for j in range(M-2):
        if A[i][j]!=B[i][j]:
            convert(i,j)
            cnt+=1
    

if check():
    print(cnt)
else:
    print(-1)
