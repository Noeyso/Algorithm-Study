## 백준_1931

N=int(input())

room = [list(map(int,input().split())) for _ in range(N)]
room=sorted(room,key=lambda x:x[0])
room=sorted(room,key=lambda x:x[1])
cnt=0
last=0
for s,e in room:
    if last<=s:
        cnt+=1
        last=e

print(cnt)
