from itertools import combinations as combi
from collections import defaultdict

def solution(info, query):
    result=[]
    info_dict = defaultdict(list)
    for i in info:
        i = i.split()
        info_key = i[:-1]
        info_val = int(i[-1])
        for j in range(5):
            for c in combi(info_key,j):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_val)

    for key in info_dict.keys():
        info_dict[key].sort()

    for qu in query:
        qu = qu.split(' ')
        query_score = int(qu[-1])
        qu = qu[:-1]

        for i in range(3):
            qu.remove('and')
        while '-' in qu:
            qu.remove('-')
        tmp_q = ''.join(qu)

        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores)>0:
                start,end=0,len(scores)
                while end>start:
                    mid = (start+end)//2
                    if scores[mid]>=query_score:
                        end=mid
                    else:
                        start=mid+1
                result.append(len(scores)-start)
        else:
            result.append(0)
        
    return result
