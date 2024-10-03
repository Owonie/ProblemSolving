function solution(k, dungeons) {
  let maxDungeons = 0;

  // 순열을 구하는 함수
  function getPermutations(arr) {
    if (arr.length === 1) return [arr];

    const perms = [];
    arr.forEach((fixed, idx, origin) => {
      const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
      const permutedRest = getPermutations(rest);
      const combined = permutedRest.map(p => [fixed, ...p]);
      perms.push(...combined);
    });
    return perms;
  }

  // 모든 던전 순서에 대해 탐험
  const permutations = getPermutations(dungeons);

  permutations.forEach((order) => {
    let currentFatigue = k; // 현재 피로도
    let dungeonCount = 0; // 탐험한 던전 수

    for (const [requiredFatigue, fatigueCost] of order) {
      // 피로도가 충분한지 확인
      if (currentFatigue >= requiredFatigue) {
        currentFatigue -= fatigueCost; // 피로도 소모
        dungeonCount++; // 탐험한 던전 수 증가
      } else {
        break; // 피로도가 부족하면 더 이상 탐험 불가
      }
    }

    // 최대 던전 수 갱신
    maxDungeons = Math.max(maxDungeons, dungeonCount);
  });

  return maxDungeons;
}