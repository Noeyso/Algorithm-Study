def solution(brown, yellow):
    answer = []
    tmp=[]
    for i in range(1,int(yellow**0.5)+1):
        if yellow%i==0:
            tmp.append([i,yellow//i])
    for t in tmp:
        w,h = t
        if (w*2+h*2+4)==brown:
            if w>h:
                return [w+2,h+2]
            else:
                return [h+2,w+2]
        
