function generateRandomNumber(){
  const N = 5;
  let str = '';
  for(let i=0;i<N;i++){
    str+=Math.floor(Math.random()*10);
  }
  return parseInt(str);
}

function checkDuplicateRate() {
  const nums = new Set();

  let count = 0;

  for (let i = 0; i < 1000; i++) {
    const randomNum = generateRandomNumber();
    if(nums.has(randomNum)){
      count+=1;
    }else{
      nums.add(randomNum);
    }
  }

  const duplicateRate = count/ 1000 *100;
  return duplicateRate;
}

console.log(`Duplicate rate: ${checkDuplicateRate()}`)


