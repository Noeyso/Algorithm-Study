## 백준_1003

T=int(input())

arr_zero=[1,0,1]
arr_one=[0,1,1]


def fib(n):
    length = len(arr_zero)
    if length<=n:
        for i in range(length,n+1):
            arr_zero.append(arr_zero[i-1]+arr_zero[i-2])
            arr_one.append(arr_one[i-1]+arr_one[i-2])
    print("%d %d"%(arr_zero[n],arr_one[n]))
            


for i in range(T):
    num=int(input())
    fib(num)

