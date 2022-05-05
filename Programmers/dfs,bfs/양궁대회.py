from collections import deque
def bfs(n,info):
    res=[]
    gap=0
    que = deque([(0,[0,0,0,0,0,0,0,0,0,0,0])])
    
    while que:
        idx,arr=que.popleft()
        if sum(arr)==n:
            apeach,lion = 0,0
            for i in range(11):
                if not(info[i]==0 and arr[i]==0):
                    if info[i]>arr[i]:
                        apeach+=(10-i)
                    else:
                        lion+=(10-i)
            if lion>apeach:
                g = lion-apeach
                if g < gap:
                    continue
                if g > gap:
                    gap=g
                    res=[]
                res.append(arr)
                
        elif sum(arr)>n:
            continue
        elif idx==10:
            copy = arr[:]
            copy[idx] = n-sum(copy)
            que.append((-1,copy))
        else:            
            copy = arr[:]
            copy[idx]=info[idx]+1
            que.append([idx+1,arr])
            que.append([idx+1,copy])
    return res
        
    
def solution(n, info):
    ans = bfs(n,info)
    
    if not ans:
        return [-1]
    if len(ans)==1:
        return ans[0]
    return ans[-1]
