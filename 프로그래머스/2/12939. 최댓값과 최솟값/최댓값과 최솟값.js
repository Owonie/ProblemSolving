function solution(s) {
    var answer = '';
    
    const number = s.split(" ");
    ansmin = Math.min(...number);
    ansmax = Math.max(...number);
    return ansmin+' '+ansmax;
    
}