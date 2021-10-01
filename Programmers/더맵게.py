import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt=0
    while scoville[0]<K:
        if len(scoville)>1:
            heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
            cnt+=1
        else:
            return -1
    return cnt
    
    '''
    while scoville[len(scoville)-1]<K:
        if len(scoville)<2:
            return -1
        scoville.sort()
        m1 = scoville.pop(0)
        m2 = scoville.pop(0)
        scoville.append(m1+m2*2)
        cnt+=1
    '''
print(solution([3, 1, 2, 9, 10, 12],7))
