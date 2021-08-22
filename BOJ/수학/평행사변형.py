## 백준_1064

from math import sqrt

ax,ay,bx,by,cx,cy = list(map(int,input().split()))

a,b,c = [ax,ay],[bx,by],[cx,cy]

roundR = []

def CalArr(x,y,z):
    d = [j+(k-l) for j,k,l in zip(x,y,z)]
    arr1 = [(i-j)*(i-j) for i,j in zip(x,z)]
    arr2 = [(i-j)*(i-j) for i,j in zip(x,d)]
    res = (sqrt(sum(arr1))+sqrt(sum(arr2)))*2
    return res

if (ax-bx)==(ax-cx)==0 or (ay-by)==(ay-cy)==0:
    print(-1.0)
elif (ay-by)*(ax-cx)==(ay-cy)*(ax-bx):
    print(-1.0)
else:
    roundR.append(CalArr(a,b,c))
    roundR.append(CalArr(b,c,a))
    roundR.append(CalArr(c,a,b))
    print(max(roundR)-min(roundR))
