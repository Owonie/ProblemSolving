function solution(n)
{
    let result = n
    let ans = 0;
    while(result > 0) {
        if(result % 2 === 1) {
            ans++;    
            result--;
        }
        else {
            result = result / 2;
        }
    }
    return ans;
}
