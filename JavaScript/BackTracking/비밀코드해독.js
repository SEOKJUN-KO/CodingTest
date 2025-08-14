let answer = []
let question = []
let answerCnt = 0

function calculate(set) {
    let flag = true
    for( let i = 0; i < question.length; i++) {
        let cnt = 0        
        for( let j = 0; j < 5; j++) {
            if ( set.has(question[i][j]) ) {
                cnt += 1
            }
        }
        if( cnt !== answer[i]) {
            flag = false
            break
        }
    }
    if (flag) { answerCnt += 1 }
}

function backtracking(n, now, set) {
    if ( set.size >= 5 || now >= n+1 ) {
        if (set.size === 5) { calculate(set) }
        return 
    }
    for(let i = now; i <= n; i++) {
        if (!set.has(i)) {
            set.add(i)
            backtracking(n, i+1, set)
            set.delete(i)
        }
    }
}

function solution(n, q, ans) {
    question = q
    answer = ans
    backtracking(n, 1, new Set())
    return answerCnt;
}