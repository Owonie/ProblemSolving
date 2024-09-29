function solution(k, tangerine) {
    var sell= 0;
    var answer = 0;
    var hashMap = {};
    for(var i = 0; i < tangerine.length; i++) {
        if(!hashMap[tangerine[i]]) {
            hashMap[tangerine[i]] = 0;
        }
        hashMap[tangerine[i]] += 1
    }
    const arr = Object.values(hashMap);
    arr.sort((a,b)=> b-a);
    var j = 0;
    while(sell < k) {
        sell += arr[j];
        answer++;
        j++;
    }
    if(tangerine.length === k) {
        answer = arr.length;
    }
    return answer;
}