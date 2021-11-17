from itertools import permutations
import re

def solution(expression):
    nums= re.findall('\d+',expression)
    nums= list(map(int,nums))
    operator = re.findall('[-+*]',expression)
    ops = list(set(operator))
    
    combi = list(permutations(ops,len(ops)))

    result=[]
    
    for comb in combi:
        nArr = nums[:]
        oArr = operator[:]
        for c in comb:
            rg=0
            while c in oArr:
                idx= oArr.index(c,rg)
                if c=="+":
                    nArr[idx]+=nArr[idx+1]
                elif c=="-":
                    nArr[idx]-=nArr[idx+1]
                elif c=="*":
                    nArr[idx]*=nArr[idx+1]
                del nArr[idx+1]
                del oArr[idx]
                rg=idx
        result.append(abs(nArr[0]))
    
    return max(result)
