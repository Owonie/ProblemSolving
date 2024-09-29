function solution(n,a,b)
{
    var A = Math.min(a,b);
    var B = Math.max(a,b);
    const arrA = [A];
    const arrB = [B];
    
    var answer = 0; 
    
    var flag = false;
    while(!flag) {
        if(Math.min(A,B) % 2 === 1 && Math.min(A,B)+1 === Math.max(A,B)) {
            flag = true;
        }
        answer++;
        if(A % 2 === 0) {
            A /= 2;
        }else {
             A = (A+1) / 2;
        }
        if(B % 2 === 0) {
            B /= 2;
        }
        else{
            B = (B+1)/2;
        }
    }
    return answer;
}