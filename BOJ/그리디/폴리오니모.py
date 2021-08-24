## 백준_1343

S = input()

board = S.split('.')
res=[]
isFalse=False


for b in board:
    m = len(b)//4
    r = len(b)%4
    result=''

    if m!=0:
        result+=('AAAA'*m)
        m-=4*m
    if r!=0:
        m=r//2
        if r%2!=0:
            isFalse=True
            break
        else:
            result+=('BB'*m)
    res.append(result)


if isFalse:
    print(-1)
else:
    print('.'.join(res))
'''

S=S.replace("XXXX","AAAA")
S=S.replace("XX","BB")

if 'X' in S:
    print(-1)
else:
    print(S)
'''
