/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let ans = 0;
    let tmp = [];
    for(let i=0;i<s.length;i++){
        w = s[i];
        if(tmp.includes(w)){
            ans = ans>tmp.length?ans:tmp.length;
            while(true){
                tmp.shift();
                if(!tmp.includes(w)){
                   break;
                }
            }
        };
        tmp.push(w);
    }
    ans = ans>tmp.length?ans:tmp.length;
    return ans;
};
