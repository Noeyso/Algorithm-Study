function solution(players, callings) {
  const rankMap = {}
  players.forEach((name,index)=>rankMap[name]=index)
  
  for(let player of callings){
      let rank = rankMap[player];
      let frontPlayer = players[rank-1];
      rankMap[player]-=1
      rankMap[frontPlayer]+=1
      players[rank] = frontPlayer
      players[rank-1] = player
  }    

  return players;
}

//https://school.programmers.co.kr/learn/courses/30/lessons/178871