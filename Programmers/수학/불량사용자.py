from itertools import permutations

def isBanned(users,banned_id):
    for i in range(len(banned_id)):
        if len(users[i])!=len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j]=="*":
                continue
            if banned_id[i][j]!=users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    shuffle = list(permutations(user_id,len(banned_id)))
    banned_set=[]
    
    for users in shuffle:
        if not isBanned(users,banned_id):
            continue
        else:
            users = set(users)
            if users not in banned_set:
                banned_set.append(users)        
            
    return len(banned_set)
