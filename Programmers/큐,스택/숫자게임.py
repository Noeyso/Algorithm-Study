def solution(A, B):
    cnt=0
    A.sort()
    B.sort()
    for i in range(len(B)):
        n1=A.pop()
        n2=B.pop()
        if n2>n1:
            cnt+=1
        else:
            B.append(n2)
        
    return cnt
