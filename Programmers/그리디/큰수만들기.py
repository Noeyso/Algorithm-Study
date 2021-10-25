def solution(number, k):
    ans=[]

    for num in number:
        while k>0 and ans and ans[-1]<num:
            ans.pop()
            k-=1
        ans.append(num)

    return ''.join(ans[:len(ans)-k])

