## 백준_1057

from sys import stdin
from collections import deque

N,kim,im = map(int,stdin.readline().split())
R=0

while kim!=im:
    kim -=kim//2
    im -= im//2
    R+=1
print(R)

