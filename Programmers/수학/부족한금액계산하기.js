function solution(price, money, count) {
    let total = price*count*(count+1)/2-money;
    
    return total>0?total:0;
}
