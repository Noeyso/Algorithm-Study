## 백준_1251 : 단어 나누기 (구현, 문자열, 브루트포스, 정렬)

word = list(input())
answer =[]
tmp=[]

for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        w1 = word[:i]
        w2 = word[i:j]
        w3 = word[j:]
        w1.reverse()
        w2.reverse()
        w3.reverse()
        tmp.append(w1+w2+w3)
    for w in tmp:
        answer.append(''.join(w))
print(sorted(answer)[0])
