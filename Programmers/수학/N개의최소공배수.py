def gcd(n,m):
    while m:
        n,m=m,n%m
    return n
def lcm(n,m):
    return (n*m)//gcd(n,m)


def solution(arr):
    answer = 0
    if len(arr)==1:
        return arr[0]
    
    arr.sort(reverse=True)
    while arr:
        n1 = arr.pop()
        n2 = arr.pop()
        arr.append(lcm(n1,n2))
        if len(arr)==1:
            answer = arr.pop()
    return answer
