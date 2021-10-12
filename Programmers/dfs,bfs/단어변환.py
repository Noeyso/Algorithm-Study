from collections import deque

def compareWord(word1,word2):
    cnt=0
    for i in range(len(word1)):
        if word1[i]!=word2[i]:
            cnt+=1
    if cnt==1:
        return True
    return False

def bfs(curr,words,visited,target):
    que = deque()
    que.append((curr,0))
    while que:
        w=que.popleft()
        if w[0]==target:
            return w[1]

        for i in range(len(words)):
            if compareWord(w[0],words[i]) and visited[i]==0:
                que.append((words[i],w[1]+1))
                visited[i]=1
    return 0
def solution(begin, target, words):
    answer = 0
    visited=[0 for _ in range(len(words))]
    if target not in words:
        return 0
    
    return bfs(begin,words,visited,target)


