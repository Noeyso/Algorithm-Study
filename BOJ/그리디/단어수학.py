##백준_1339

from sys import stdin
input = stdin.readline

N=int(input())

words=[input().rstrip() for _ in range(N)]
word_dict={}
arr=[]

for i in range(N):
    for j in range(len(words[i])):
        if words[i][j] in word_dict:
            word_dict[words[i][j]]+= 10**(len(words[i])-1-j)
        else:
            word_dict[words[i][j]] = 10**(len(words[i])-1-j)

for value in word_dict.values():
    arr.append(value)

arr.sort(reverse=True)

total=0
number=9
for i in arr:
    total+=number*i
    number-=1
    
print(total)
