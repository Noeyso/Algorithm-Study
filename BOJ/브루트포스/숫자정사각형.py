## 백준_1051

from sys import stdin

N,M = map(int,stdin.readline().split())

arr=[]
for i in range(N):
    s = stdin.readline().rstrip()
    arr.append(list(s))

tmp=N if N<M else M

isTrue=True

while isTrue:
    for i in range(N-tmp+1):
        for j in range(M-tmp+1):
            if arr[i][j]==arr[i+tmp-1][j]==arr[i][j+tmp-1]==arr[i+tmp-1][j+tmp-1]:
                print(tmp*tmp)
                isTrue=False
                break
        if not isTrue:
            break
    tmp-=1
