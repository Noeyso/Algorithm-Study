##백준_3085 : 사탕게임

from sys import stdin
input = stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

def check(board):
    cnt_max=0
    for i in range(N):
        cnt_row=1
        cnt_col=1
        for j in range(N-1):
            if board[i][j]==board[i][j+1]:
                cnt_row+=1
            else:
                cnt_max=max(cnt_max,cnt_row)
                cnt_row=1

            if board[j][i]==board[j+1][i]:
                cnt_col+=1
            else:
                cnt_max=max(cnt_max,cnt_col)
                cnt_col=1
        cnt_max=max(cnt_max,cnt_row,cnt_col)
    return cnt_max

cnt = 0
for i in range(N):
    r_cnt=0
    c_cnt=0
    for j in range(N):
        if j+1<N:
            if board[i][j]==board[i][j+1]:
                r_cnt+=1
            else:
                r_cnt=1
                board[i][j],board[i][j+1]=board[i][j+1],board[i][j]
                tmp = check(board)
                if tmp>cnt:
                    cnt=tmp
                board[i][j],board[i][j+1]=board[i][j+1],board[i][j]
        if i+1<N:
            if board[i][j]==board[i+1][j]:
                c_cnt+=1
            else:
                c_cnt=1
                board[i][j],board[i+1][j]=board[i+1][j],board[i][j]
                tmp = check(board)
                if tmp>cnt:
                    cnt=tmp
                board[i][j],board[i+1][j]=board[i+1][j],board[i][j]
    cnt=max(cnt,r_cnt,c_cnt)
            
print(cnt)
