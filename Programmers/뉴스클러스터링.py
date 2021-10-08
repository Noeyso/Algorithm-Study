from collections import Counter

def solution(str1, str2):
    str1=str1.upper()
    str2=str2.upper()
    s1,s2=[],[]
    for i in range(len(str1)-1):
        s=str1[i:i+2]
        if s.isalpha():
            s1.append(s)
    for i in range(len(str2)-1):
        s=str2[i:i+2]
        if s.isalpha():
            s2.append(s)
    Counter1 = Counter(s1)
    Counter2 = Counter(s2)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(inter)==0 and len(union)==0:
        return 65536
    else:
        return int(len(inter)/len(union)*65536)

print(solution("Fr","french"))
