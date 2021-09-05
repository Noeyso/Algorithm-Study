## 백준_11399

N = int(input())
time = list(map(int,input().split()))
time.sort()

result=[0]*(N+1)
for i in range(N):
    result[i+1]=result[i]+time[i]

print(sum(result))

