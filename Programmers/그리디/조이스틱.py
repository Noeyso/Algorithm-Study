def solution(name):
    answer = 0
    a_count=0
    idx=0
    length = len(name)
    
    for i in range(length):
        if 0<i<length:
            answer+=1
        
        if name[i]=='A':
            if a_count==0:
                idx=abs(i-1)
            a_count+=1
            continue

        if a_count!=0:
            if idx<0:
                idx=0
            if i-idx> idx+1:
                answer-=(i-idx-idx-1)
            a_count=0
        
        n= ord(name[i])
        a_sub = n-ord('A')
        z_sub = ord('Z')-n+1
        
        if a_sub<z_sub:
            answer+=a_sub
        else:
            answer+=z_sub
        
        
    return answer
