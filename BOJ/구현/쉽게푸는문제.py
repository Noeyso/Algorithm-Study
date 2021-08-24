## 백준_1292

a,b = map(int,input().split())

arr=[]
i=1
while len(arr)<b+1:
    tmp=[i]*i
    arr+=tmp
    i+=1
print(sum(arr[a-1:b]))
