def solution(enroll, referral, seller, amount):
    answer = []
    tree={'-':'root'}
    sell={'-':0}
    for child,parent in zip(enroll,referral):
        sell[child]=0
        tree[child]=parent

    for i in range(len(seller)):
        child=seller[i]
        parent=tree[child]
        money=amount[i]*100
        sell[child]+=money
        while True:
            discount=money//10
            if discount==0:
                break
            sell[child]-=discount
            sell[parent]+=discount
            child=parent
            parent=tree[child]
            money=discount
            if parent=='root':
                break
    for person in enroll:
        answer.append(sell[person])
        

    return answer
