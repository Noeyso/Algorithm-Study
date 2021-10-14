def solution(tickets):
    di={}
    tickets.sort(reverse=True)
    for t1,t2 in tickets:
        if t1 in di:
            di[t1].append(t2)
        else:
            di[t1]=[t2]
    que=['ICN']
    res=[]
    while que:
        s = que[-1]
        if s not in di or len(di[s])==0:
            res.append(que.pop())
        else:
            que.append(di[s].pop())
    res.reverse()
            
    return res

print(solution([["ICN", "SFO"], ["ICN", "ATL"],
                ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
