import itertools

def solution(land, P, Q):
    land_list = list(itertools.chain.from_iterable(land))
    land_list.sort()
    N = len(land_list)
    cost = (sum(land_list)-N*land_list[0])*Q
    answer = cost
    
    
    for i in range(1,N):
        if land_list[i]!=land_list[i-1]:
            cost=cost+(land_list[i]-land_list[i-1])*P*i-(land_list[i]-land_list[i-1])*Q*(N-i)
            if answer<cost:
                break
            answer = min(answer,cost)
    
    return answer
