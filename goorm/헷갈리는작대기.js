// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

let sum_one=0,sum_i=0,sum_l=0,sum_bar=0;
rl.on("line", function(line) {
	//console.log("Hello Goorm! Your input is", line);
	for(let i=0;i<line.length;i++){
		switch(line[i]){
			case "1":
				sum_one+=1;
				break;
			case "I":
				sum_i+=1;
				break;
			case "l":
				sum_l+=1;
				break;
			case "|":
				sum_bar+=1;
				break;
			default:
				break;
		}
	}
	console.log(sum_one);
	console.log(sum_i);
	console.log(sum_l);
	console.log(sum_bar);
	
	rl.close();
}).on("close", function() {
	process.exit();
});
