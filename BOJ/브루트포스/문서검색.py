## 백준_1543

from sys import stdin

S=stdin.readline().rstrip()
W=stdin.readline().rstrip()

idx=0
cnt=0
for i in range(0,len(S)):
    if W in S[idx:]:
        cnt+=1
        f = S.index(W,idx)
        idx=(f+len(W))
    else:
        break
print(cnt)

'''
while idx<=len(S)-len(word):
    if S[idx:idx+len(W)]==word:
        cnt+=1
        i+=len(word)
    else:
        i+=1
print(count)
