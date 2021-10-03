from collections import deque

def solution(s):
    answer=deque([])
    str_arr = deque(list(s))
    answer.append(str_arr.popleft())

    while str_arr:
        num = str_arr.popleft()
        if len(answer)==0:
            answer.append(num)
            continue
        n = answer.pop()
        if n!=num:
            answer.append(n)
            answer.append(num)
    if len(answer)==0:
        return 1
    else:
        return 0

print(solution("abbcdaadca"))
