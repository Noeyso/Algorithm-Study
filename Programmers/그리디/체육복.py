def solution(n, lost, reserve):
    
    s_lost = set(lost)-set(reserve)
    s_reserve = set(reserve)-set(lost)
    
    for r in s_reserve:
        if r-1 in s_lost:
            s_lost.remove(r-1)
        elif r+1 in s_lost:
            s_lost.remove(r+1)

    answer=n-len(s_lost)
            
    return answer

print(solution(7,[2,3,5,7],[3,4,6]))
