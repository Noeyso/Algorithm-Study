def solution(n, stations, w):
    answer = 0
    interval = w*2+1
    prev = 1
    for st in stations:
        start=st-w
        end=st+w
        if (start-prev)%interval==0:
            answer+=(start-prev)//interval
        else:
            answer+=(start-prev)//interval+1
        prev = end+1
    if prev<=n:
        if (n+1-prev)%interval==0:
            answer+=(n+1-prev)//interval
        else:
            answer+=(n+1-prev)//interval+1
    return answer
  
def solution(n, stations, w):
  answer = 0
  idx=0
  loc=1

  while (loc<=n):
      if idx<len(stations) and loc>=stations[idx]-w:
          loc = stations[idx]+w+1
          idx+=1
      else:
          loc+=2*w+1
          answer+=1

  return answer
