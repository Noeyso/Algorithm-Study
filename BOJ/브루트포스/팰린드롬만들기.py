##백준_1254

from sys import stdin
input= stdin.readline

String = input().rstrip()

for i in range(len(String)):
    if String[i:]==String[i:][::-1]:
        print(len(String)+i)
        break
