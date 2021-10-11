import sys
sys.setrecursionlimit(10**6)

def preorder(arr,answer):
    node = arr[0]
    arrY1=[]
    arrY2=[]
    
    for i in range(1,len(arr)):
        if node[0]>arr[i][0]:
            arrY1.append(arr[i])
        else:
            arrY2.append(arr[i])
    answer.append(node[2])
    if len(arrY1)>0:
        preorder(arrY1,answer)
    if len(arrY2)>0:
        preorder(arrY2,answer)
    return

def postorder(arr,answer):
    node = arr[0]
    arrY1=[]
    arrY2=[]
    
    for i in range(1,len(arr)):
        if node[0]>arr[i][0]:
            arrY1.append(arr[i])
        else:
            arrY2.append(arr[i])
    if len(arrY1)>0:
        postorder(arrY1,answer)
    if len(arrY2)>0:
        postorder(arrY2,answer)
    answer.append(node[2])
    return


def solution(nodeinfo):
    preanswer=[]
    postanswer=[]
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    array = sorted(nodeinfo,key=lambda x:(-x[1],x[0]))

    preorder(array,preanswer)
    postorder(array,postanswer)
    
    return [preanswer,postanswer]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
