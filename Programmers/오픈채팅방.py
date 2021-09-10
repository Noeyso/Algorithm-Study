def solution(record):
    answer = []
    dict_id={}
    re = []
    for s in record:
        s_arr=list(s.split())
        re.append(s_arr)
        if len(s_arr)==3:
            dict_id[s_arr[1]]=s_arr[2]
    while re:
        arr=re.pop(0)
        if arr[0]=='Enter':
            answer.append("{}님이 들어왔습니다.".format(dict_id[arr[1]]))
        if arr[0]=='Leave':
            answer.append("{}님이 나갔습니다.".format(dict_id[arr[1]]))
    
    return answer
