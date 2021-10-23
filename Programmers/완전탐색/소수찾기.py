from itertools import permutations

def isPrime(num):
    if num==1 or num==0:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    arr = list(numbers)
    res=[]
    for i in range(1,len(arr)+1):
        res+=list(permutations(arr,i))
    arr_nums=[]
    for i in range(len(res)):
        li = res[i]
        num = int(''.join(li))
        if not num in arr_nums:
            if isPrime(num):
                arr_nums.append(num)
                answer+=1
        
    return answer
