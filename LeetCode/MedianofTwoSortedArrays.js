
//javascript 의 sort() 함수 사용
var findMedianSortedArrays = function(nums1, nums2) {
    
    let compare=(i,j)=>{
        return i-j;
    }
    
    let arr = nums1.concat(nums2).sort(compare);
    let len = arr.length;
    
    if(len%2==0){ 
        return (arr[len/2-1]+arr[len/2])/2;
    }
    return arr[Math.floor(len/2)];
};

//이진 탐색을 사용해서 정렬
var findMedianSortedArrays = function(nums1, nums2) {
    let arr=[];
    const len1=nums1.length;
    const len2=nums2.length; 
    let totLen = len1+len2;
    
    if(totLen == 1 ){
        return len1==1?nums1[0]:nums2[0];
    }
    
    let arrLen = totLen % 2 ==0? (totLen)/2+1:Math.ceil(totLen/2);
    
    let i=0;
    let j=0;
    
    while(arr.length<arrLen){
        if(i<len1 && j<len2){
            if(nums1[i]<nums2[j]){
                arr.push(nums1[i]);
                i++;
            }else{
                arr.push(nums2[j]);
                j++;
            }
        }else if(i>=len1){
            arr.push(nums2[j]);
            j++;
        }else{
            arr.push(nums1[i]);
            i++;
        }
    }
    
    return totLen%2==0?(arr[arr.length-1]+arr[arr.length-2])/2:arr[arr.length-1];
};
