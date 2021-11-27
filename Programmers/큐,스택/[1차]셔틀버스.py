from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    ## timetable을 분단위로 전환
    new_timetable=[]
    for time in timetable:
        new_timetable.append(int(time[:2])*60+int(time[3:]))
    new_timetable.sort(reverse=True)

    ## bus 시간 테이블 만들기
    bus_table = [540+(i*t) for i in range(n)]

    tmp_answer=0
    bus_idx=0
    
    ## 첫차부터 막차까지 움직인다.
    while bus_idx<n:
        stack=[]
        bus_onboard=0
        # 해당하는 버스에 정원이 다 찰때까지 인원을 세준다.
        while bus_onboard!=m:
            if len(new_timetable)>=1 and new_timetable[len(new_timetable)-1]<=bus_table[bus_idx]:
                bus_onboard+=1
                stack.append(new_timetable.pop())
            else:
                break
        if bus_idx==len(bus_table)-1:
            if bus_onboard==m:
                tmp_answer=stack.pop()-1
            else:
                tmp_answer=bus_table[bus_idx]
        bus_idx+=1

    if tmp_answer//60 <10:
        answer+='0'+str(tmp_answer//60)
    else:
        answer+=str(tmp_answer//60)
    answer+=":"
    if tmp_answer%60 <10:
        answer+='0'+str(tmp_answer%60)
    else:
        answer+=str(tmp_answer%60)
        
        
    return answer
