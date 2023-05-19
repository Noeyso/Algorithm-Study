/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
  let y=0;
  let cnt=0;
  let visited = Array.from(Array(numRows),()=>[]);
  let arr = s.split('');
  let state='down';
  while(cnt<s.length){
      visited[y].push(arr[cnt]);
      if(y===numRows-1){
        y-=1;
        state='up';
      }else if(y===0){
        y+=1;
        state='down';
      }else if(state==='down'){
          y+=1;
      }else{
          y-=1;
      }
      cnt+=1;
  }
  let result = '';
  visited.forEach((v)=>{
      result+=v.join('');
  });
  return result;
};

console.log(convert('PAYPALISHIRING',3))