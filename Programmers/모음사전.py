from itertools import product

def solution(word):
    words=[]
    for i in range(5):
        for j in product("AEIOU",repeat=i+1):
            words.append(''.join(j))
    words.sort()
            
    return words.index(word)+1

"""
def solution(word):
   alpha=['A','E','I','O','U']
   alpha_set = set(alpha)

   for _ in range(4):
       temp=[]
       for s in alpha_set:
           for a in alpha:
               temp.append(s+a)
       alpha_set.update(temp)
       print(alpha_set)
   return sorted(list(alpha_set)).index(word)+1
"""
