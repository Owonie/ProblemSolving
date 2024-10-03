function solution(progresses, speeds) {
    var answer = [];
    // 하나씩 더해서 제일 앞이 100이 되면 해당 스택을 비운다 -> 해당 작업 뒤에 100보다 큰놈들 다 찾는다.
    // 업무 다 쳐내고 배포 -> 다음 작업부터 다시 더한다.
    
    // 일단 하나씩 더하는 것 -> 하루하루
    let start = 0;
    let end = progresses.length;
      for(let i = 0; i < end; i++) {
          let day = 0;
          if(progresses[i] < 100) {
             day = Math.ceil((100 - progresses[i])/speeds[i]);
          }  
          progresses[i] = 100;
          let deploy = 1;
          let flag = true;
          for(let j = i+1; j < end; j++) {
              progresses[j] += day * speeds[j];  
              if(progresses[j] >= 100 && flag) {
                  deploy++;
                  i++;
              } else {
                  flag = false;
              }
          }
          console.log('day',day,'deploy',deploy,'prg',progresses)
          answer.push(deploy);
      }
    return answer;
}