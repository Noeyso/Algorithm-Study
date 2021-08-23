## 백준_1181 : 단어정렬 (정렬)
'''
## 내가 구현한 코드
N=int(input())
words=set()

for i in range(N):
    words.add(input())
words=list(words)
words.sort(key=lambda x:len(x))

tmp=[]
res=[]
w_len=1
for i in range(len(words)):
    w = words[i]
    if w_len!=len(w):
        tmp.sort()
        res+=tmp
        tmp=[]
        w_len=len(w)
    tmp.append(w)
    if i==len(words)-1:
        tmp.sort()
        res+=tmp

        
for w in res:
    print(w)

'''
N=int(input())
words_list=[]

for _ in range(N):
    word = str(input())
    word_count = len(word)
    words_list.append((word,word_count))
##중복 제거
words_list = list(set(words_list))

##단어 숫자 정렬 > 단어 알파벳 정렬
words_list.sort(key=lambda word:(word[1],word[0]))

for word in words_list:
    print(word[0])
