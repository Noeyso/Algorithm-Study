## 백준_1920

from sys import stdin

N=int(stdin.readline())
nums=sorted(map(int,stdin.readline().split()))
M=int(stdin.readline())
m = list(map(int,stdin.readline().split()))


def findNumber(l,arr,s,e):
    if s>e:
        return 0
    k=(s+e)//2
    if l==arr[k]:
        return 1
    elif l<arr[k]:
        return findNumber(l,arr,s,k-1)
    else:
        return findNumber(l,arr,k+1,e)

for l in m:
    s=0
    e=N-1
    print(findNumber(l,nums,s,e))
