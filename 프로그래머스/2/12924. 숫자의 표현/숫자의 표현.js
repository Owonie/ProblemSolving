function solution(n) {
    var answer = 1;
    if(n % 2 === 1) {
        for(var i = 1; i < (n + 1) / 2; i++){
            var result = 0;
            for(var j = i; result < n ; j++) {
                result += j;
            }
            if(result === n) {
                answer += 1
            }
        }
        return answer;
    }
    
    for(var i = 1; i < (n + 1) / 2; i++){
        var result = 0;
        for(var j = i; result < n; j++) {
            result += j;
        }
        if(result === n) {
            answer += 1
        }
    }
    return answer;
}