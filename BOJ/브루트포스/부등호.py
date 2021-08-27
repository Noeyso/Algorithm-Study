## 백준_2529

from sys import stdin
from collections import deque

N = int(stdin.readline())
op =stdin.readline().split()
c=[False]*10
mx,mn="",""

def possible(i,j,k):
    if k=='<':
        return i<j
    if k=='>':
        return i>j
    return True

def solve(cnt,s):
    global mx,mn
    if cnt==N+1:
        if len(mn)==0:
            mn=s
        else:
            mx=s
        return
    for i in range(10):
        if c[i]==False:
            if cnt==0 or possible(s[-1],str(i),op[cnt-1]):
                c[i]=True
                solve(cnt+1,s+str(i))
                c[i]=False
solve(0,"")
print(mx)
print(mn)
                  
