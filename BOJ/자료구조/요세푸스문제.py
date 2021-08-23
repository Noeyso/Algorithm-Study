## 백준_1158 : 요세푸스문제(자료구조_큐)

N,K = map(int,input().split())

arr=list(range(1,N+1))
res=[]
num=0

for i in range(N):
    num+=K-1
    if num>=len(arr):
        num=num%len(arr)
    res.append(str(arr.pop(num)))

print("<",", ".join(res)[:],">",sep="")
