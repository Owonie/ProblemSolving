function solution(citations) {
    let answer = 0;
    let set = new Set(citations);
    let arr = [...set];
    arr.sort((a,b) => a-b);
    for(let i = 0; i < arr[arr.length-1]; i++) {
        console.log(i)
        let count = 0;
        for(let j = 0; j < citations.length; j++) {
            if(citations[j] >= i) {
                count++;
            }
        }
        if(count >= i && citations.length - count <= i ) {
            answer = Math.max(i,answer);
        }
    }
    return answer;
}