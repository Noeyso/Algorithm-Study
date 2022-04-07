import math

def solution(n, k):
    answer =[]
    lst = [x for x in range(1,n+1)]

    while n!=0:
        temp = math.factorial(n-1)
        index = int(k//temp)
        k=k%temp

        if k==0:
            answer.append(lst.pop(index-1))
        else:
            answer.append(lst.pop(index))
        n-=1

    return answer
