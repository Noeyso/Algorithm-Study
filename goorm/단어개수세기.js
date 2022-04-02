// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

let space= 1;
let word=0;
rl.on("line", function(line) {
	//console.log("Hello Goorm! Your input is", line);
	for (let i=0;i<line.length;i++){
		if(line[i]===" "){
			space+=1;
		}else{
			if(space>0){
				word+=1;
				space=0;
			}
		}
	}
	console.log(word);
	rl.close();
}).on("close", function() {
	process.exit();
});
