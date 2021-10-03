def split(s):
    que=[]
    op,cl = 0,0
    isCorrect = True
    while s:
        c = s.pop(0)
        que.append(c)
        if c=="(":
            op+=1
            if op==cl:
                isCorrect=False
                break
        elif c==")":
            cl+=1
            if op==cl:
                break
    return que,s,isCorrect

def reverse(strings):
    r = {"(":")",")":"("}
    return [r[s] for s in strings]

def recursive(s):
    if not s:
        return []
    u,v,isCorrect = split(s)
    if isCorrect:
        return u+recursive(v)
    else:
        u=u[1:-1]
        return ["("]+recursive(v)+[")"]+reverse(u)

def solution(p):
    answer=recursive(list(p))
            
    return "".join(answer)

print(solution("()))((()"))
