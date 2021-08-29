##백준_14888

N = int(input())
arr = list(map(int,input().split()))
opr = list(map(int,input().split()))

min_,max_ = 1e9,-1e9

def dfs(i,res,add,sub,mul,div):
    global max_,min_
    if i==N:
        max_=max(res,max_)
        min_=min(res,min_)
        return
    else:
        if add:
            dfs(i+1,res+arr[i],add-1,sub,mul,div)
        if sub:
            dfs(i+1,res-arr[i],add,sub-1,mul,div)
        if mul:
            dfs(i+1,res*arr[i],add,sub,mul-1,div)
        if div:
            dfs(i+1,-(int(-res//arr[i]))if res<0 else int(res//arr[i]),add,sub,mul,div-1)

dfs(1,arr[0],opr[0],opr[1],opr[2],opr[3])
print(max_)
print(min_)
