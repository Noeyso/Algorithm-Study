import math
def solution(fees, records):
    answer = []
    table = []
    last_time = 23*60+59
    for record in records:
        r = record.split(" ")
        table.append([r[1],r[0],r[2]])
    table.sort()

    tmp=table[0][0]
    state = table[0][1]
    
    total = 0
    prev=0
    
    for t in table:
        time = t[1].split(":")
        minute = int(time[0])*60+int(time[1])
        if tmp!=t[0]:
            if state=="IN":
                total+=last_time-prev
            if total<=fees[0]:
                answer.append(fees[1])
            else:
                answer.append(fees[1]+math.ceil((total-fees[0])/fees[2])*fees[3])
            tmp=t[0]
            prev=minute
            total=0
            state=t[2]
        else:
            if state=="IN":
                total+=(minute-prev)
                
            else:
                prev = minute
            state=t[2]
    if state=="IN":
        total+=(last_time-prev)
    if total<=fees[0]:
        answer.append(fees[1])
    else:
        answer.append(fees[1]+math.ceil((total-fees[0])/fees[2])*fees[3])
            
    return answer
