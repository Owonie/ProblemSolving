function solution(want, number, discount) {
    var answer = 0;
    
    for(var i = 0; i <= discount.length - 10; i++) {
        const map = new Map();
        for(var k = 0; k < want.length; k++) {
            map.set(want[k], number[k]);
        }
        const days = discount.slice(i,i+10);
        for(var j =0; j < days.length; j++) {
            const item = map.get(discount[i+j]);
            if(item) {
                map.set(discount[i+j],item - 1);
            }
            if(map.get(discount[i+j]) === 0) {
                map.delete(discount[i+j]);
            }
        }
        if(map.size === 0) {
            answer++;
        }
        map.clear()
    }
    return answer;
}