function solution(s) {
    var cnt = 0;
    var zero = 0;
    var temp = s;
    while(temp.length > 1) {
        cnt++;
        zero += (temp.split("0")).length - 1;
        temp ="1" * (temp.length - ((temp.split("0")).length - 1))
        temp = temp.toString(2);
    }
    return [cnt,zero];
}