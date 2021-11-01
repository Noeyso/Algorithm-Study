from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        candidates=[]
        new_menu={}
        for order in orders:
            for li in combinations(list(order),c):
                res = ''.join(sorted(li))
                if res not in candidates:
                    candidates.append(res)
                else:
                    if res not in new_menu:
                        new_menu[res]=2
                    else:
                        new_menu[res]+=1
        sorted_menu = sorted(new_menu.items(),key=lambda x:x[1])
        if sorted_menu:
            max_value = sorted_menu[-1][1]
            while sorted_menu:
                menu,value = sorted_menu.pop()
                if value==max_value:
                    answer.append(menu)
        
    return sorted(answer)
