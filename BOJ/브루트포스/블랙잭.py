##백준_2798

from sys import stdin
input = stdin.readline

N,M = map(int,input().split())

tmp=M
tmp_sum=0
cards =list(map(int,input().rsplit()))

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            s = cards[i]+cards[j]+cards[k]
            if s>M:
                continue
            if abs(M-s)<tmp:
                tmp=abs(M-s)
                tmp_sum=s

                
print(tmp_sum)
