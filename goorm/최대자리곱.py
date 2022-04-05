def solution(n):
    length = len(str(n))
    digit = [0]*length
    mul =1

    for i in range(length-1,-1,-1):
        dg= n//10**i
        digit[i]=dg
        n-=dg*10**i
        mul*=dg
    if digit[length-1]==1:
        return 9**(length-1)
    
    accum=1
    for i in range(length-1,-1,-1):
        if digit[i]==0:
            accum//=digit[i-1]
            accum*=digit[i-1]-1
            mul = max(mul,accum*(9**(i+1)))
        else:
            mul = max(mul,accum*(digit[i]-1)*(9**i))
            accum*=digit[i]

    return mul


n = int(input())

print(solution(n))
