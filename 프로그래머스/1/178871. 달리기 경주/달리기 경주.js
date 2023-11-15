function solution(players, callings) {
    const map = new Map();
    players.forEach((name,index)=> {
        map.set(name,index);
    })
    callings.forEach(name=> {
        const idx = map.get(name);
        // 다음친구
        const next = players[idx-1];
        
        // 교환
        const temp = players[idx];
        players[idx] = players[idx-1];
        players[idx-1] = temp;
        // 교환 했으니 map 초기화
        map.set(name,map.get(name)-1);
        map.set(next,map.get(name)+1);
    })
    return players;
}