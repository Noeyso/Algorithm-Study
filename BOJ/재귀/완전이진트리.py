## 백준_9934

K = int(input())
tree=list(map(int,input().split()))
nodes=[[] for i in range(K)]

def f(arr,k):
    mid=(len(arr)//2)
    nodes[k].append(arr[mid])
    if len(arr)==1:
        return
    f(arr[:mid],k+1)
    f(arr[mid+1:],k+1)
    

f(tree,0)
for i in range(K):
    print(*nodes[i])
