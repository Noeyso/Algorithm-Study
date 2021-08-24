N=int(input())

A = list(map(int,input().split()))
A_sort=[]
P=[0]*N
for i in range(len(A)):
    A_sort.append([i,A[i]])
A_sort.sort(key=lambda x:x[1])

for j in range(len(A_sort)):
    idx=A_sort[j][0]
    P[idx]=str(j)

print(' '.join(P))
