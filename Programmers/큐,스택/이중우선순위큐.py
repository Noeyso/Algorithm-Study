import heapq

def solution(operations):
    heap=[]
    for i in range(len(operations)):
        command,data = operations[i].split()
        data = int(data)
        if command=="I":
            heapq.heappush(heap,data)
        elif command=="D":
            if data==1:
                if heap:
                    max_value = max(heap)
                    heap.remove(max_value)
            else:
                if heap:
                    heapq.heappop(heap)
    if len(heap)==0:
        return [0,0]
    return [max(heap),heapq.heappop(heap)]
