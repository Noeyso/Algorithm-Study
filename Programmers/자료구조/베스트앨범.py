def solution(genres, plays):
    di={}
    di_sum={}
    res=[]
    for i in range(len(genres)):
        gen = genres[i]
        play = plays[i]
        if gen not in di:
            di[gen]=[(i,play)]
            di_sum[gen]=play
        else:
            di[gen].append((i,play))
            di_sum[gen]+=play

    di_sum = dict(sorted(di_sum.items(),key=lambda x:x[1],reverse=True))

    for k in di_sum.keys():
        arr = sorted(di[k],key=lambda x:x[1],reverse=True)[:2]
        for i,p in arr:
            res.append(i)
            
        
    return res
