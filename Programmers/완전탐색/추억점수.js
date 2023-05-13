// 나의 풀이

function solution(name, yearning, photo) {
  let answer = [];
  let names = {};
  for(let i=0;i<name.length;i++){
      names[name[i]] =yearning[i]; 
  }
  for(let ph of photo){
      let total=0;
      for(person of ph){
          if(person in names){
           total+=names[person];   
          }
      }
      answer.push(total);
  }
  return answer;
}

// 다른 사람의 풀이

function solution(name, yearning, photo) {
  let names = {};
  for(let i=0;i<name.length;i++){
      names[name[i]] =yearning[i]; 
  }
  return photo.map(ph=>ph.map(person=>names[person]?names[person]:0).reduce((acc,cur)=>acc+cur,0));
}

