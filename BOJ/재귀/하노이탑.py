##백준_1914

def hanoi(n,start,mid,to):
    if n==1:
        print(start,to)
        return
    hanoi(n-1,start,to,mid)
    print(start,to)
    hanoi(n-1,mid,start,to)

N = int(input())
print(2**N-1)
if N<=20:
    hanoi(N,1,2,3)
