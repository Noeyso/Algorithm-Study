def solution(s):
    length=[]
    result=""

    if len(s)==1:
        return 1
    
    for n in range(1,len(s)//2+1):
        cnt=1
        tmpStr=s[:n]
        for i in range(n,len(s),n):
            if s[i:i+n]==tmpStr:
                cnt+=1
            else:
                if cnt==1:
                    cnt=""
                result+=str(cnt)+tmpStr
                tmpStr=s[i:i+n]
                cnt=1
        if cnt==1:
            cnt=""
        result+=str(cnt)+tmpStr
        length.append(len(result))
        result=""
    return min(length)
