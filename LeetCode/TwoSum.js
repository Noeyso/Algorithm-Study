var twoSum = function(nums, target) {
    /* 
    시간복잡도 최대 O(n**2)
    for(let i=1;i<nums.length;i++){
       for(let j=0;j<i;j++){
            if(nums[j]+nums[i]==target){
                return [j,i];
            }
        }
    }
    */
    
    // 시간복잡도 최대 O(N)
    let numsObj={};
    for(let i=0;i<nums.length;i++){
        let current = nums[i];
        let match = target-current;
        if(match in numsObj){
            console.log(match);
            return [i,numsObj[match]];
        }else{
            numsObj[current] = i;
        }
    }
};
