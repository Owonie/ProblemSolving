function solution(n, left, right) {
    let answer = [];    
    let start = 0;
    let end = 0;
    // 시작이 뭔지
    start = Math.round(left/n);
    end = Math.round(right/n);
    for(let i = left; i <= right; i++) {
        answer.push(Math.max(Number.parseInt(i/n),i%n)+1);
    }
    return answer;
}
// left -> 시작 위치. right -> 끝나는 위치.
// 1 2  2 2  
// 1 2 3   2 2 3   3 3 3
// 1 2 3 4  2 2 3 4  3 3 3 4  4 4 4 4
// start = 1 -> i = n
// start = 2 -> i = 2 if i <= start else i = n
// 1 2 3 4 5  2 2 3 4 5  3 3 3 4 5  4 4 4 4 5  5 5 5 5 5