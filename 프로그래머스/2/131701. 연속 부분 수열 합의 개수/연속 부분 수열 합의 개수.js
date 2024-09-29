function solution(elements) {
    var answer = 0;
    var arr = [...elements,...elements];
    const map = new Map();
    var number = 0 ;
    for(var i = 0; i < elements.length; i++) {
        for(var num = 1; num < elements.length +1; num++) {
            number = 0;
            for(var j = 0; j < num; j++) {
                number += arr[j+i];
            }
            map.set(number,1);
        }
        
    }
    return map.size;
}