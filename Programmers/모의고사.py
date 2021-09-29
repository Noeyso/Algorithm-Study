def solution(answers):
    answer = []
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    score=[0,0,0,0]
    for s in answers:
        a_num,b_num,c_num=a.pop(0),b.pop(0),c.pop(0)
        if s==a_num:
            score[1]+=1
        if s==b_num:
            score[2]+=1
        if s==c_num:
            score[3]+=1
        a.append(a_num)
        b.append(b_num)
        c.append(c_num)
    max_num = max(score)
    for i in range(1,4):
        if score[i]==max_num:
            answer.append(i)
    return answer


print(solution([1,3,2,4,2]))
