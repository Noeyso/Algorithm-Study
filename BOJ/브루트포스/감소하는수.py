##백준_1038

N = int(input())

num=20
cnt=10
check=False

while True:
    if N<=10:
        check=True
        num=N
        break
    if N>1022:
        check=False
        break
    s = str(num)
    isX=True
    for i in range(len(s)-1):
        if s[i]>s[i+1]:
            continue
        else:
            isX=False
            start=s[:i]
            mid = str(int(s[i])+1)
            end='0'*(len(s)-1-i)
            num=int(start+mid+end)
            break
    if isX:
        cnt+=1
        if cnt==N:
            check=True
            break
        num+=1
    
if check:
    print(num)
else:
    print(-1)
