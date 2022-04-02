const readline = require('readline');

function solution(N,K,data){
	let count=0;
	let min=99999;
	let test=[];
	
	for (let i=0;i<N-K+1;i++){
		for (let j=0;j<N-K+1;j++){
			for(let q = i;q<i+K;q++){
				for(let r=j;r<j+K;r++){
					if(data[q][r]==='1') count++;
					
				}
			}
			test=[];
			if(count<min) min=count;
			count=0;
		}
	}
	return min;
}
(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	let T= null;
	let N= null, K=null;
	let info=null;
	
	let data=[];
	let countT=0;
	let countN=0;
	
	for await (const line of rl) {
		//console.log('Hello Goorm! Your input is', line);
		if(!T){
			T= +line;
		}else if(!N && !K){
			[N,K] = line.split(' ').map((el)=>+el);
			
		}else{
			data.push(line.split(' '));
			countN +=1;
		}
		if (countN === N){
			const res = solution(N,K,data);
			console.log(res);
			N=null;
			K=null;
			countN=0;
			data=[];
			countT += 1;
		}
		
		if (countT === T){
			rl.close();
		}
		if (T === countT){
			rl.close();
		}
	}
	
	process.exit();
})();
