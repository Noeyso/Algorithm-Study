## 백준_1966

from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())

for i in range(T):
    N,M = map(int,input().split())
    docs = list(map(int,input().split()))
    idx=list(range(N))
    idx[M]='target'

    #순서
    order=0
    
    while True:
        if docs[0]==max(docs):
            order+=1
            
            if idx[0]=='target':
                print(order)
                break
            else:
                docs.pop(0)
                idx.pop(0)  
        else:
            docs.append(docs.pop(0))
            idx.append(idx.pop(0))
            
