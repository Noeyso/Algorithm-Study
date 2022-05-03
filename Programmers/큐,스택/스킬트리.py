def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    for skills in skill_trees:
        skill_list= list(skill)
        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    answer-=1
                    break
            
    return answer
