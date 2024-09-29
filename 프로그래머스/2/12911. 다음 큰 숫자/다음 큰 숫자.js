function solution(n) {
    var answer = n;
    var nBin = n.toString(2);
    var flag = 0;
    while(flag < 1) {
        answer++;
        const ansBin = answer.toString(2);
        if(ansBin.split('1').length === nBin.split('1').length){
            flag++;
        }
    }
    
    return answer;
}