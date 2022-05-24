def solution(rows, columns, queries):
    answer = []
    board = [[0 for _ in range(columns)]for _ in range(rows)]
    k=1
    for i in range(rows):
        for j in range(columns):
            board[i][j]=k
            k+=1

    d = {'R':(0,1,'D'),'L':(0,-1,'U'),'U':(-1,0,-1),'D':(1,0,'L')}

    for  x1,y1,x2,y2 in queries:
        tmp = board[x1-1][y1-1]
        mini = tmp
        
        for k in range(x1-1,x2-1):
            test = board[k+1][y1-1]
            board[k][y1-1] = test
            mini = min(mini,test)
        for k in range(y1-1,y2-1):
            test = board[x2-1][k+1]
            board[x2-1][k] = test
            mini = min(mini,test)
        for k in range(x2-1,x1-1,-1):
            test = board[k-1][y2-1]
            board[k][y2-1] = test
            mini = min(mini,test)
        for k in range(y2-1,y1-1,-1):
            test = board[x1-1][k-1]
            board[x1-1][k] = test
            mini = min(mini,test)
        board[x1-1][y1]=tmp
        answer.append(mini)
                
    return answer
