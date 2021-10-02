def gcd(n,m):
    if m%n==0:
        return n
    else:
        return gcd(m%n,n)
    
def gcm(n,m,d):
    return int(n*m/d)
    

def solution(n, m):
    g = gcd(n,m)
    answer = [g,gcm(n,m,g)]
    return answer
