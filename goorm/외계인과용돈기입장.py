# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N,M = map(int,input().split())
arr = list(map(int,input().split()))
accum=0
for i in range(N):
	accum+=arr[i]
	arr[i]=accum
arr.insert(0,0)


for i in range(M):
	a,b = map(int,input().split())
	hap = arr[b]-arr[a-1]
	if hap>0:
		print("+"+str(hap))
	else:
		print(str(hap))
