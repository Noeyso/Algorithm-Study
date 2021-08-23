## 백준_1094 : 막대기(비트마스킹)

X = int(input())

n=64
count=0
bar=[64]
while True:
    if X==n:
        count+=1
        break
    else:
        if sum(bar)>=X:
            if n==1:
                tot=0
                for i in bar:
                    if tot!=X and X&i==i:
                        tot+=i
                        count+=1
                break
            else:
                bar.pop()
                n=n>>1
                if n >=X:
                    bar.append(n)
                else:
                    bar = bar+[n,n]

print(count)

'''
## 2진법으로 나타냈을때 1이 몇개있냐?! => 1의 개수만 알면 된다.
while X!=0:
    if X%2==1:
        count+=1
    X=X//2
print(count)
'''
