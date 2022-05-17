def solution(lines):
    answer = 0
    start_time=[]
    end_time=[]
    
    for line in lines:
        time = line.split(' ')
        start_time.append(get_start_time(time[1],time[2]))
        end_time.append(get_time(time[1]))
    for i in range(len(lines)):
        cnt=0
        cur_end_time = end_time[i]
        for j in range(i,len(lines)):
            if cur_end_time>start_time[j]-1000:
                cnt+=1
        answer = max(answer,cnt)
    return answer

def get_time(time):
    hour = int(time[:2])*3600
    minute = int(time[3:5])*60
    second = int(time[6:8])
    milisecond = int(time[9:])
    return (hour+minute+second)*1000+milisecond

def get_start_time(time,dur):
    T = dur[:-1]
    dur_time = int(float(T)*1000)
    return get_time(time)-dur_time+1
