def solution(people, limit):
    people.sort()
    answer = 0
    start,end=0,len(people)-1
    weight=people[end]
    while start<=end:
        if start==end:
            answer+=1
            break
        if people[end]+people[start]>limit:
            answer+=1
            end-=1
        else:
            answer+=1
            start+=1
            end-=1

    return answer
