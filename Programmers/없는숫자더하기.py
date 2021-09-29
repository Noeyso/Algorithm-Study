def solution(numbers):
    nums=[0,1,2,3,4,5,6,7,8,9]
    res=list(set(nums)-set(numbers)) 
    return sum(res)

'''
def solution(numbers):
    return 45 - sum(numbers)
'''
print(solution([5,8,4,0,6,7,9]))
