
# 특정 원소가 속한 집합을 찾기
def find(parent,x):
    if parent[x]==x:
        return x
    parent[x]=find(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기 (간선 연결한다고 생각!)
def union(parent,a,b):
    rootA = find(parent,a)
    rootB = find(parent,b)

    if rootA<rootB:
        parent[rootB] = rootA
    else:
        parent[rootA]=rootB

        
def solution(n, costs):
    parent=[i for i in range(n)]
    result=0

    costs.sort(key=lambda x:x[2])

    for c in costs:
        a,b,cost = c
        #사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
        if find(parent,a)!=find(parent,b):
            union(parent,a,b)
            result+=cost
    
    
    return result
