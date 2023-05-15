// 나의 풀이

function solution(today, terms, privacies) {
    let answer = [];
    const termsInfo ={}; 
    let arr = today.split('.').map((d)=>parseInt(d));

    for(let term of terms){
        const [type,period] = term.split(' ');
        termsInfo[type] = parseInt(period);
    }
    for(let i=0;i<privacies.length;i++){
        let [tyear,tmonth,tday] = arr;
        const [date,term] = privacies[i].split(' ');
        const dateArr = date.split('.');
        const  [year,month,day]  = dateArr.map((d)=>parseInt(d));
        const period = termsInfo[term];

        if(tyear>year){
            tmonth+=(tyear-year)*12;
        }
        const diff=tmonth-month;
        if(diff>period){
            answer.push(i+1);
            continue;
        }else if(diff<period){
            continue;
        }else{
            if(tday-day>=0){
                answer.push(i+1);
            }
        }

    }
    return answer;
}

//다른 사람의 풀이
function solution(today, terms, privacies) {
  var answer = [];
  var [year, month, date] = today.split(".").map(Number);
  var todates = year * 12 * 28 + month * 28 + date;
  var t = {};
  terms.forEach((e) => {
    let [a, b] = e.split(" ");
    t[a] = Number(b);
  });
  privacies.forEach((e, i) => {
    var [day, term] = e.split(" ");
    day = day.split(".").map(Number);
    var dates = day[0] * 12 * 28 + day[1] * 28 + day[2] + t[term] * 28;
    if (dates <= todates) answer.push(i + 1);
  });
  return answer;
}