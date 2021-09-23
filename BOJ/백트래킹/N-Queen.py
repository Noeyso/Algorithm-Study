##백준_9663
N = int(input())

row,left,right=[0 for _ in range(N)],[0 for _ in range(2*N-1)],[0 for _ in range(2*N-1)]
result=0

def queen(x):
    global result
    if x==N:
        result+=1
        return
    for col in range(N):
        if row[col]+left[x+col]+right[N-1+x-col]==0:
            row[col]=left[x+col]=right[N-1+x-col]=1
            queen(x+1)
            row[col]=left[x+col]=right[N-1+x-col]=0
            

queen(0)
print(result)
