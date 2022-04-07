import math

def findNum(nums,n):
    head = 0
    tail = len(nums)-1
    center = (head+tail)//2

    while nums[center]!=n:
        if head>tail: return 0

        if nums[center]<n:
            head = center+1
            center= (head+tail)//2
        else:
            tail = center-1
            center= (head+tail)//2
    return 1

N = int(input())
nums = list(map(int,input().split()))
nums.sort()
max_num = max(nums)
min_num = min(nums)

M = int(input())
test = list(map(int,input().split()))

for n in test:
    if n>max_num or n<min_num:
        print(0)
    else:
        print(findNum(nums,n))
