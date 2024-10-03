function solution(arr1, arr2) {
    let answer = [];

    // arr1의 열 수와 arr2의 행 수가 같은지 확인
    if (arr1[0].length !== arr2.length) {
        throw new Error('행렬 곱셈이 불가능합니다. arr1의 열 수와 arr2의 행 수가 동일해야 합니다.');
    }

    for (let i = 0; i < arr1.length; i++) {
        let temp = [];
        for (let j = 0; j < arr2[0].length; j++) {
            let sum = 0;
            for (let k = 0; k < arr1[0].length; k++) {
                sum += arr1[i][k] * arr2[k][j];
            }
            temp.push(sum);
        }
        answer.push(temp);
    }

    return answer;
}
