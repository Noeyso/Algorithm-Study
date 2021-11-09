def solution(gems):
    answer = []
    jnum=len(set(gems))
    sp,ep=0,0
    min_length=len(gems)+1
    visited={}

    while ep<len(gems):
        if gems[ep] not in visited:
            visited[gems[ep]]=1
        else:
            visited[gems[ep]]+=1
        ep+=1
        if len(visited)==jnum:
            while sp<ep:
                if visited[gems[sp]]>1:
                    visited[gems[sp]]-=1
                    sp+=1
                elif min_length>ep-sp:
                    min_length=ep-sp
                    answer=[sp+1,ep]
                else:
                    break
        
    return answer
