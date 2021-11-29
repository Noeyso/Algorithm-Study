def solution(routes):
    answer = 1
    routes.sort()
    inCar=routes.pop()[0]
    while routes:
        route=routes.pop()
        if route[1]>=inCar:
            continue
        else:
            answer+=1
            inCar=route[0]
        
    return answer
