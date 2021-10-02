import math

def solution(w,h):
    answer = 1
    if w==h:
        return w*h-w
    if w==1 or h==1:
        return 0
    
    return w*h-(w+h-math.gcd(w,h))

print(solution(8,12))
