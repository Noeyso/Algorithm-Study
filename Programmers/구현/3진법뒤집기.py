function solution(n) {
    let num = makeTernary(n);
    return makeDecimal(num);
}

function makeTernary(n){
    let res = parseInt(n/3);
    let rem = n%3;
    let ans = [rem];
    
    while (res!=0){
        rem = res%3;
        res = parseInt(res/3);
        ans.push(rem);
    }
    return ans;
}
function makeDecimal(arr){
    let res=0;
    let len = arr.length-1;
    for(let i=0;i<=len;i++){
        res+=arr[i]*(3**(len-i));
    }
    return res;
}
