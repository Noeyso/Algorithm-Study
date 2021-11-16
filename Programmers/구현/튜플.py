import re

def solution(s):
    answer = []
    res=s.split(',{')
    res.sort(key=len)
    for i in res:
        nums = re.findall("\d+",i)
        for j in nums:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
