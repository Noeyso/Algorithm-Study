def solution(stones, k):
    left=1
    right=max(stones)
    answer = 0
    while left<=right:
        zero=0

        mid=(left+right)//2

        for stone in stones:
            if stone-mid<=0:
                zero+=1
            else:
                zero=0
            if zero>=k:
                break

        if zero<k:
            left=mid+1
        else:
            answer=mid
            right=mid-1
    
    return answer
