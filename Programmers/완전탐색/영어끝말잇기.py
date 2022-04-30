def solution(n, words):
    for p in range(1,len(words)):
        if words[p][0]!=words[p-1][-1] or words[p] in words[:p]:
            return [(p%n)+1,(p//n)+1]
    return [0,0]
  
  
  
  def solution(n, words):
    tmp =[words[0]]
    turn=1
    order = 1
    prev=words[0][-1]
    
    for i in range(1,len(words)):
        order+=1
        if order>n:
            order=1
            turn+=1
        if words[i][0]!=prev:
            return [order,turn]
        elif words[i] in tmp:
            return [order,turn]
        else:
            prev=words[i][-1]
        tmp.append(words[i])
    return [0,0]
