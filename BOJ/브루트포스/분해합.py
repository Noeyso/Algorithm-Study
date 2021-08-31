## 백준_2231

num = int(input())

res=0
for i in range(1,num+1):
    arr= list(map(int,str(i)))
    res=i+sum(arr)
    if res==num:
        print(i)
        break
    if i==num:
        print(0)
        
