##백준_5585

N=int(input())

change=[500,100,50,10,5,1]

money=1000-N

cnt=0
r=0
for m in change:
    n= money//m
    if n>0:
        cnt+=n
        r=money%m
        money-=m*n

print(cnt)
