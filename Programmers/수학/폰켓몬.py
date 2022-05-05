'''
def solution(nums):

    ans=len(set(nums))
    leng = len(nums)//2

    if ans>leng:
        return leng
    else:
        return ans
'''
def solution(nums):
    return min(len(nums)/2,len(set(nums)))
print(solution([3,3,3,2,2,2]))
