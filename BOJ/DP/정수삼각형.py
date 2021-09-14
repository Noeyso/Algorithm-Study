##백준_1932 : 정수삼각형

from sys import stdin
input=stdin.readline

N =int(input())

triangle = [list(map(int,input().rsplit())) for _ in range(N)]
cal = [[0 for j in range(len(triangle[i]))] for i in range(N)]
cal[0]=triangle[0]

for i in range(N-1):
    for j in range(len(triangle[i])):
        cal[i+1][j]=max(cal[i+1][j],cal[i][j]+triangle[i+1][j])
        cal[i+1][j+1]=max(cal[i+1][j+1],cal[i][j]+triangle[i+1][j+1])
            
print(max(cal[N-1]))
