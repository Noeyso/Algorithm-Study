/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let tmp = "";
    let maxLen=1;
    let maxStr=s[0];
    
    if(s.length==1){
        return s;
    }
    
    for(let i=0;i<s.length;i++){
        tmp=s[i];
        for(let j=i+1;j<s.length;j++){
            tmp+=s[j];
            let tmpLen = tmp.length;
            if(tmpLen<maxLen){
                continue;
            }
            if(isPalin(tmp)){
                maxLen=tmpLen;
                maxStr=tmp;
            };
        }
    }
    return maxStr;
};

function isPalin(str){
    let len = str.length;
    for(let i=0;i<len/2;i++){
        if(str[i]!==str[len-1-i]){
            return false
        }
    }
    return true;
}
