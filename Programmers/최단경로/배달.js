// N개의 마을, K시간 이하로 배달이 가능한 마을에서만 주문 받기 , 도로의 정보 road
// 마을의 개수 return

function solution(N, road, K) {
  const visited = Array(N+1).fill(Infinity);
  const lines = Array.from(Array(N+1),()=>[]);

  road.forEach((value)=>{
    let [a,b,c] = value;
    lines[a].push({to:b,cost:c});
    lines[b].push({to:a,cost:c});
  })

  let queue = [{to:1,cost:0}];
  visited[1]=0;

  while(queue.length){
    let {to}  = queue.pop();
    lines[to].forEach(next=>{
      if(visited[next.to]>visited[to]+next.cost){
        visited[next.to] = visited[to]+next.cost;
        queue.push(next);
      }
    })
  }

  return visited.filter((item)=>item<=K).length;
}

console.log(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3));