'''
def solution(N, stages):
    answer = [[i,0] for i in range(N+2)]
    num = len(stages)
    print(answer)
    
    stages.sort()
    stage=1
    tmp_num=0
    tmp=num
    for i in range(num):
        if stages[i]!=stage:
            answer[stage][1]=tmp_num/tmp
            stage=stages[i]
            tmp-=tmp_num
            tmp_num=1
        else:
            tmp_num+=1
    answer[stage][1]=tmp_num/tmp
    answer.sort(key = lambda x:x[1],reverse=True)
    res=[]
    for s,f in answer:
        if s>N or s==0:
            continue
        res.append(s)
        
    return res
    '''
def solution(N,stages):
    result={}
    denominator = len(stages)
    for stage in range(1,N+1):
        if denominator!=0:
            count = stages.count(stage)
            result[stage]=count/denominator
            denominator-=count
        else:
            result[stage]=0
    return sorted(result,key=lambda x:result[x],reverse=True)

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
