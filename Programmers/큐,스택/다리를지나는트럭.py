def solution(bridge_length, weight, truck_weights):
    time=0
    passed=[]
    passing=[0]*bridge_length
    length = len(truck_weights)

    while len(passed)<length:
        time+=1
        last = passing.pop(0)
        if last!=0:
            passed.append(last)
        if len(truck_weights)>0:
            if sum(passing)+truck_weights[0]<=weight:
                passing.append(truck_weights.pop(0))
            else:
                passing.append(0)
        
    return time
