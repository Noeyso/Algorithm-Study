## 백준_4949 : 스택

from sys import stdin

while True:
    S = stdin.readline().rstrip()
    if S=='.':
        break
    stack=[]
    temp=True
    for i in S:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==']':
            if stack!=[]:
                b=stack.pop()
                if b=='(':
                    temp=False
                    break
            else:
                temp=False
                break
        elif i==')':
            if stack!=[]:
                b=stack.pop()
                if b=='[':
                    temp=False
                    break
            else:
                temp=False
                break
    if temp and not stack:
        print("yes")
    else:
        print("no")
