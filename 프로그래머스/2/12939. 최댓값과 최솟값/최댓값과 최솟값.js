function solution(s) {
    var answer = '';
    
    const number = s.split(" ").map(number => Number(number));
    ansmin = Math.min(...number);
    ansmax = Math.max(...number);
    return ansmin+' '+ansmax;
    
}