def solution(citations):
    citations.sort()
    length = len(citations)
    for i in range(length,-1,-1):
        for j in range(length):
            if citations[j]>=i:
                if length-j<i:
                    break
                return i
