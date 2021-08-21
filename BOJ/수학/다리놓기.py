## 백준_1010

tc = int(input())

result=[]


def factorial(n):
    num=1
    for i in range(1,n+1):
        num*=i
    return num

for i in range(tc):
    N,M=map(int,input().split())
    if N>M:
        result.append(0)
    elif N==M:
        result.append(1)
    else:
        result.append(factorial(M)//factorial(M-N)//factorial(N))


    
for i in range(tc):
    print(result[i])
