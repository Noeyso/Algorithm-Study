## 백준_1205 : 등수 구하기(구현, 정렬)

N,score,P=map(int,input().split())

if N==0:
    print(1)
else:
    score_arr = list(map(int,input().split()))
    if N==P and score_arr[-1]>=score:
        print(-1)
    else:
        idx = N+1
        for i in range(N):
            if score_arr[i] <= score:
                idx=i+1
                break
        print(idx)
