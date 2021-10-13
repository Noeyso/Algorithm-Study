from itertools import combinations,product

def solution(clothes):
    di={}        
    for i in range(len(clothes)):
        try:
            di[clothes[i][1]]+=1
        except KeyError:
            di[clothes[i][1]]=1
    lst = list(di.values())
    if len(lst)==1:
        return len(clothes)
    res=0
    for i in range(2,len(lst)+1):
        arr=list(combinations(lst,i))
        for j in range(len(arr)):
            cnt=1
            for k in range(len(arr[j])):
                cnt*=arr[j][k]
            res+=cnt
    return res+len(clothes)

'''
def solution(clothes):
    clothes_type={}

    for c,t in clothes:
        if t not in clothes_type:
            clothes_type[t]=2
        else:
            clothes_type[t]+=1
    cnt=1
    for num in clothes_type.values():
        cnt*=num
    return cnt-1
'''
'''
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"],
                ["yellowhat", "headgear"],["green_turban", "headgear"],["sweater","tshirts"]]))
'''
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
