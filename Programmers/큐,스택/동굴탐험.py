def solution(n, path, order):
    tree=[[] for _ in range(n)]
    for p1,p2 in path:
        tree[p1].append(p2)
        tree[p2].append(p1)
    orders = [0 for i in range(n)]
    for pre,post in order:
        orders[post]=pre
    
    num_visit=0
    visited=[False for _ in range(n)]
    que=[0]
    
    after = {}

    while que:
        tmp = que.pop()
        if orders[tmp] and not visited[orders[tmp]]:
            after[orders[tmp]]=tmp
            continue
        visited[tmp]=True
        num_visit+=1
        
        for t in tree[tmp]:
            if not visited[t]:
                que.append(t)
        
        if tmp in after:
            que.append(after[tmp])
    return n==num_visit
