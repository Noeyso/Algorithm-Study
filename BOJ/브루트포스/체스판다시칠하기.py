## 백준_1018

N,M = map(int,input().split())

board=[]
for i in range(N):
    board.append(input())

min_board=[]
for n in range(N-7):
    for m in range(M-7):
        black_idx=0
        white_idx=0
        for i in range(n,n+8):
            for j in range(m,m+8):
                if (i+j)%2==0:
                    if board[i][j]!='B':
                        black_idx+=1
                    else:
                        white_idx+=1
                else:
                    if board[i][j]!='B':
                        white_idx+=1
                    else:
                        black_idx+=1
        min_board.append(black_idx)
        min_board.append(white_idx)


print(min(min_board))
