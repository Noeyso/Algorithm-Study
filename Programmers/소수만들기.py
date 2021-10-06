from itertools import combinations
def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def solution(nums):
    answer = 0
    combi = list(combinations(nums,3))
    for i in range(len(combi)):
        if isPrime(sum(combi[i])):
            answer+=1

    return answer


print(solution([1,2,3,4]))
