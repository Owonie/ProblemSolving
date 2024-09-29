function solution(s){
    var answer = true;
    var left = 0;
    var right = 0;
    a = [...s];
    if(a.length === 0) {return false;}
    for(var i = 0; i < a.length; i++) {
        if(a[i] === '(') {
            left++;
        }
        else {
            right++;
        }
        if(left < right) {
            answer = false;
        }
    }
    if(left !== right) {
        answer = false;
    }
    return answer;
}