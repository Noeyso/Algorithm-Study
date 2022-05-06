def solution(n):
    answer = []
    arr = [[0]*i for i in range(1,n+1)]
    move=[[1,0],[0,1],[-1,-1]]
    mi=0
    r,c=0,0
    tmp=1
    arr[0][0]=1
    if n==1:
        return [1]
    for i in range(n,0,-1):
        for j in range(i):
            r+=move[mi][0]
            c+=move[mi][1]
            tmp+=1
            arr[r][c]=tmp
            if tmp==n:
                break
        mi+=1
        if mi>2:
            mi=0
    for nums in arr:
        for item in nums:
            answer.append(item)
    return answer
