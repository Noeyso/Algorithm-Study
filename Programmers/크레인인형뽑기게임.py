def solution(board, moves):
    answer = 0
    ch_board=list(map(list,zip(*board)))
    res=[]
    
    for mov in moves:
        n=0
        if ch_board[mov-1]:
            while n==0:
                n=ch_board[mov-1].pop(0)
            res.append(n)
    idx=1
    toys=[]
    cnt=0
    while idx<len(res):
        if res[idx]==res[idx-1]:
            res.pop(idx)
            res.pop(idx-1)
            cnt+=2
            idx=1
        else:
            idx+=1
    return cnt
