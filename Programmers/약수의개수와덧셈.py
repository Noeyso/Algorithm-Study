                
'''
def solution(left, right):
    answer = 0
    cnt=[0]*(right+1)

    for i in range(1,right+1):
        for j in range(i,right+1):
            if j%i==0:
                cnt[j]+=1
        if i>=left and i<=right:
            if cnt[i]%2==0:
                answer+=i
            else:
                answer-=i
    return answer

'''

def solution(left,right):
    answer=0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer-=i
        else:
            answer+=i
    return answer


print(solution(1,2))
