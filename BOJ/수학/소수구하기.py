## 백준_1929

a,b = map(int,input().split())


li = [False,False]+[True]*(b-1)
primes=[]

for i in range(2,b+1):
    if li[i]:
        primes.append(i)
        for j in range(2*i,b+1,i):
            li[j]=False

for n in primes:
    if n>=a:
        print(n)
