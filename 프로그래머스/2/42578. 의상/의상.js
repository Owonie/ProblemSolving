function solution(clothes) {
    var answer = 1;
    let map = new Map();
    for(let i = 0; i < clothes.length; i++) {
        if(!map.has(clothes[i][1])) {
            map.set(clothes[i][1],[clothes[i][0]])
        } else {
            const temp = map.get(clothes[i][1]);
            temp.push(clothes[i][0]);
             map.set(clothes[i][1],temp);
        }
    }
    console.log(map);
    const iterators = map.values();
    for(let i = 0; i < map.size; i++) {
        const result= iterators.next().value;
        console.log(result.length)
        if(Array.isArray(result)) {
             answer *= result.length+1
        }
    }

    return answer-1;
}