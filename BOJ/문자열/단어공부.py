## 백준_1157

word = input().upper()

s = word.upper()
w_set =set()
for i in s:
    w_set.add(i)
tmp=0
result=''

for i in w_set:
    count = s.count(i)
    if count>tmp:
        tmp=count
        result=i
    elif count==tmp:
        result="?"
        break

print(result)

'''
## 다른 풀이

words = input().upper()
unique_words = list(set(words))

cnt_list=[]
for x in unique_words:
    cnt = words.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list))>1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])

'''
