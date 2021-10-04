
def solution(lottos, win_nums):
    lott = [6,6,5,4,3,2,1]
    w = len(set(lottos))-len(set(lottos)-set(win_nums))
    zero = lottos.count(0)
    answer=[lott[(w+zero)],lott[w]]
    return answer

'''
def solution(lottos, win_nums):
    lott = [6,6,5,4,3,2,1]
    zero = lottos.count(0)
    cnt=0
    for x in win_nums:
        if x in lottos:
            cnt+=1
    return lott[zero+cnt],lott[cnt]
'''
    

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
