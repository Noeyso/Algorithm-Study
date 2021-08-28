## 백준_10815

from sys import stdin

N=int(stdin.readline())
n_arr=sorted(map(int,stdin.readline().split()))
M=int(stdin.readline())
m_arr=list(map(int,stdin.readline().split()))


def binary(n,s,e):
    if s>e:
        return '0'
    k=(s+e)//2
    if n_arr[k]==n:
        return '1'
    elif n<n_arr[k]:
        return binary(n,s,k-1)
    else:
        return binary(n,k+1,e)
        

arr=[]

for n in m_arr:
    s=0
    e=N-1
    arr.append(binary(n,s,e))
print(' '.join(arr))
