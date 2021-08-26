## 백준_1676 : 팩토리얼 0의 개수

from sys import stdin

N = int(stdin.readline())

count=0
while N>=5:
    count+=N//5

    N//=5
print(count)
