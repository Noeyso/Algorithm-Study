L,C = map(int,input().split())
check=[0 for i in range(C)]
arr=[]

alpha = list(map(str,input().split()))
alpha.sort()


def makeString(length,idx):
    if length==L:
        vo=0
        co=0
        for i in range(L):
            if arr[i] in 'aeiou':vo+=1
            else: co+=1
        if vo>=1 and co>=2:
            print("".join(arr))
    for i in range(idx,C):
        if check[i]==0:
            arr.append(alpha[i])
            check[i]=1
            makeString(length+1,i+1)
            check[i]=0
            del arr[-1]
        

makeString(0,0)
