## 백준_1748 : 수 이어 쓰기 1

N=int(input())

if N<10:
    print(N)
else:
    n=9
    length =len(str(N))
    n+=(N-(10**(length-1)-1))*length
    for i in range(2,length):
        n+=((10**(i)-1)-(10**(i-1)-1))*i
    print(n)
