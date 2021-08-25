## 백준_4539 : 반올림 (수학, 구현)

from sys import stdin
from math import pow

N = int(stdin.readline())

result =[]
def printNum(num):
    x = list(map(int,str(num)))

    if len(x)==1:
        print(*x,sep='')
    else:
        length=len(x)
        for i in range(length-1,0,-1):
            if x[i]>=5:
                x[i-1]=x[i-1]+1
                x[i]=0
            else:
                x[i]=0
        print(*x,sep='')

for n in range(N):
    num= int(stdin.readline())
    printNum(num)
