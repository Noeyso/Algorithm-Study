## 백준_1406 : 스택

from sys import stdin

S = list(stdin.readline().strip())

N = int(stdin.readline())

cur = len(S)

S2=[]
for i in range(N):
    c = stdin.readline().strip()

    if c[0]=='P':
        S.append(c[2])
    elif c[0]=='L' and S!=[]:
        S2.append(S.pop())
    elif c[0]=='D' and S2!=[]:
        S.append(S2.pop())
    elif c[0]=='B' and S!=[]:
        S.pop()
    
print(''.join(S+list(reversed(S2))))       
    

